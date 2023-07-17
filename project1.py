from flask import Flask, render_template, request, redirect
import random
from flask_sqlalchemy import SQLAlchemy
import mysql.connector


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness2.db'
app.config["DEBUG"] = True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    muscle = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"{self.id}-{self.name}-{self.age}-{self.weight}-{self.height}-{self.muscle}"


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        weight = request.form['weight']
        height = request.form['height']
        muscle = request.form['muscle']

    return render_template('index1.html')



@app.route('/hydration')
def hydration():
    return render_template('hydration.html')

@app.route('/index')
def home():
    return render_template('login.html')


connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='lieutenant07',
    database='practice1'
    )

cursor = connection.cursor()

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cursor = connection.cursor()
    query = "insert into users(username, password) values(%s, %s)"
    values = (username, password)
    cursor.execute(query, values)
    connection.commit()

    return "Data submitted successfully!!!"



@app.route('/diet', methods=['GET','POST'])
def diet():
    return render_template('diet.html')


# Dictionary of meal options for weight gain and weight loss
weight_gain_diets = {
    'Breakfast': [
        'Protein smoothie with oats and fruits',
        'Egg and vegetable scramble with whole wheat toast',
        'Greek yogurt with granola and berries'
    ],
    'Lunch': [
        'Grilled chicken with brown rice and roasted vegetables',
        'Quinoa salad with avocado and chickpeas',
        'Turkey wrap with mixed greens and hummus'
    ],
    'Snack': [
        'Almonds and dried fruits',
        'Protein bar',
        'Cottage cheese with sliced fruits'
    ],
    'Dinner': [
        'Salmon with quinoa and steamed asparagus',
        'Lean beef stir-fry with brown rice',
        'Grilled tofu with roasted sweet potatoes and green beans'
    ]
}

weight_loss_diets = {
    'Breakfast': [
        'Avocado toast with poached eggs',
        'Oatmeal with berries and almond butter',
        'Chia seed pudding with mixed fruits'
    ],
    'Lunch': [
        'Grilled chicken salad with mixed greens and vinaigrette',
        'Spinach and feta stuffed bell peppers',
        'Veggie wrap with hummus and sprouts'
    ],
    'Snack': [
        'Apple slices with almond butter',
        'Carrot sticks with hummus',
        'Greek yogurt with honey and nuts'
    ],
    'Dinner': [
        'Baked salmon with steamed vegetables',
        'Shrimp stir-fry with brown rice noodles',
        'Vegetable curry with quinoa'
    ]
}


@app.route('/diet_result', methods=['POST'])
def diet_result():
    diet_plan = request.form.get('dietPlan')


    if diet_plan == 'weightGain':
        diet = weight_gain_diets

    elif diet_plan == 'weightLoss':
        diet = weight_loss_diets
    else:
        diet = {}

    selected_diets = {meal: random.choice(diet[meal]) for meal in diet}



    return render_template('diet_result.html', diets=selected_diets)




@app.route('/bmi')
def bmi():
    return render_template('bmi.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    height = float(request.form['height'])
    weight = float(request.form['weight'])

    # Calculate BMI
    bmi = weight / (height ** 2)

    return render_template('cal_bmi.html', bmi=bmi)



@app.route('/exercises')
def exercises():
    return render_template('exercises.html')


connection2 = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='lieutenant07',
    database='practice2'
    )

cursor2 = connection2.cursor()

@app.route('/generate_schedule', methods=['POST'])
def generate_schedule():
    name = request.form.get('name')
    age = int(request.form.get('age'))
    weight = request.form.get('weight')
    height = request.form.get('height')
    muscle = request.form.get('muscle')

    cursor2 = connection2.cursor()
    query2 = "insert into users2(name, age, weight, height, muscle) values(%s, %s, %s, %s, %s)"
    values2 = (name, age, weight, height, muscle)
    cursor2.execute(query2, values2)
    connection2.commit()


    rev = '''
    Welcome {{ name }} to our fitness regime....\n
    As per your personal information, height is {{ height }} meters and weight is {{ weight }} kgs.\n
    So you need a weight type schedule....
    We have built a split muscle workout schedule for you.\n
    I hope you SWEAT HARD, BUDDY!!!!
    '''

    rev = rev.replace("{{ name }}", name)
    rev = rev.replace("{{ height }}", height)
    rev = rev.replace("{{ weight }}", weight)

    l1 = ['shoulders', 'chest', 'biceps', 'triceps', 'legs', 'back', 'abs']
    l2 = ['cardio', 'body weight training']

    if muscle in l1 or muscle in l2:
        schedule = generate_workout_schedule(muscle)
        return render_template('bmi2.html', name=name, rev=rev, muscle=muscle, schedule=schedule)
    else:
        return "Choice is inappropriate"

def generate_workout_schedule(muscle):
    if muscle == 'shoulders':
        shoulderwarmup = ["Weight rotation    -->2 X 20 Reps", "Light raises    -->2 X 20 Reps", "Stick or strap stretch    -->2 X 20 Reps"]
        shoulderlight = ["Front raise    -->3 X 12-15 Reps", "Rear delts    -->3 X 15 Reps", "Upright bar    -->3 X 12-15 Reps"]
        shouldermiddle = ["Lateral raises    -->3 X 15-20 Reps", "Rear raises    -->3 X 12-15 Reps", "Incline dumbbells    -->3 X 12-15 Reps", "Upright bar raises    -->3 X 15 Reps", "Hammer top press    -->3 X 15 Reps"]
        shoulderheavy = ["Shoulder press    -->3 X 12-15 Reps", "Front bar raises    -->3 X 15 Reps", "Rear cable pulls    -->3 X 12-15 Reps"]
        return [random.choice(shoulderwarmup), random.choice(shoulderlight), random.choice(shouldermiddle), random.choice(shoulderheavy)]
    elif muscle == 'chest':
        chestwarmup = ["Light dumbbells    -->2 X 20 Reps", "Dips    -->2 X 10 Reps", "Light chest extension    -->2 X 15 Reps"]
        chestlight = ["Chest extension    -->3 X 15 Reps", "Cable fly    -->3 X 12-15 Reps", "Incline/Decline/Flat dumbbells    -->3 X 12-15 Reps"]
        chestmiddle = ["Upper cable fly    -->3 X 12-15 Reps", "Dumbbell fly    -->3 X 12-15 Reps", "Double bar    -->3 X 15 Reps"]
        chestheavy = ["Incline bench press    -->3 X 12-15 Reps", "Decline bench press    -->3 X 12-15 Reps", "Flat bench press    -->3 X 12-15 Reps"]
        return [random.choice(chestwarmup), random.choice(chestlight), random.choice(chestmiddle), random.choice(chestheavy)]
    elif muscle == 'biceps':
        bicepswarmup = ["Light dumbbell curls/hammers    -->2 X 20 Reps", "Chin-ups    -->2 X 10 Reps"]
        bicepslight = ["Flat bar cable curls    -->3 X 12-15 Reps", "Zig-zag bar cable curls    -->3 X 12-15 Reps", "Rope pulls    -->3 X 12-15 Reps", "Concentration curls    -->3 X 12-15 Reps"]
        bicepsmiddle = ["Dumbbell curls    -->3 X 15 Reps", "Hammer raises    -->3 X 15 Reps", "Inclined dumbbell curls    -->3 X 12-15 Reps", "Preacher curls    -->3 X 12-15 Reps"]
        bicepsheavy = ["Flat bar curls    -->3 X 12-15 Reps", "Zig-zag bar curls    -->3 X 12-15 Reps", "Lying down curls    -->3 X 12-15 Reps", "Standing cable pulls    -->3 X 12-15 Reps", "Preacher hammer    -->3 X 12-15 Reps"]
        return [random.choice(bicepswarmup), random.choice(bicepslight), random.choice(bicepsmiddle), random.choice(bicepsheavy)]
    elif muscle == 'triceps':
        tricepswarmup = ["Light dumbbell stretch    -->2 X 20 Reps", "Close hand Dips    -->2 X 10 Reps", "Single hand dumbbell    -->2 X 20 Reps"]
        tricepslight = ["Dumbbell raises    -->3 X 12-15 Reps", "Raises with V-Bar    -->3 X 15 Reps", "Forward pushdown    -->3 X 12-15 Reps", "Double bar    -->3 X 12-15 Reps"]
        tricepsmiddle = ["Weighted back dips    -->3 X 20-30 Reps", "Rope pushdown    -->3 X 12-15 Reps", "Bended dumbbell pushback    -->3 X 12-15 Reps"]
        tricepsheavy = ["Close grip    -->3 X 12-15 Reps", "Hammer bar push    -->3 X 12-15 Reps", "Belgium skull crusher    -->3 X 12-15 Reps"]
        return [random.choice(tricepswarmup), random.choice(tricepslight), random.choice(tricepsmiddle), random.choice(tricepsheavy)]
    elif muscle == 'legs':
        legswarmup = ["Free squats    -->2 X 30-50 Reps", "Side stretches    -->2 X 30 Reps", "farmers walk    -->2 X 30 Reps", "Dumbbell calf raises    -->2 X 20 Reps"]
        legslight = ["Kettle bell squats    -->3 X 20-30 Reps", "Single leg split squats    -->3 X 20-30 Reps", "Hip thrusts    -->3 X 20-40 Reps", "Goblet squats    -->3 X 20-30 Reps"]
        legsmiddle = ["Legs extension    -->3 X 15-30 Reps", "Quad raises    -->3 X 15-25 Reps", "Hamstring pulls    -->3 X 15-20 Reps", "Standing lunges    -->3 X 20-30 Reps", "Seated Calf raises    -->3 X 25-40 Reps"]
        legsheavy = ["Leg press    -->3 X 15-25 Reps", "Heavy squats    -->3 X 15-20 Reps", "Walking dumbbell/Bar lunges    -->3 X 15-20 Reps", "Front dumbbell squats    -->3 X 15-20 Reps","Hamstring deadlift    -->3 X 15-20 Reps"]
        return [random.choice(legswarmup), random.choice(legslight), random.choice(legsmiddle),random.choice(legsheavy)]
    elif muscle == 'back':
        backwarmup = ["Rope stretches    -->2 X 20 Reps", "Weight rotations    -->2 X 20 Reps", "Stick or strap rotations    -->2 X 20 Reps"]
        backlight = ["Pull-ups    -->3 X 15-25 Reps", "Front rope pulls    -->3 X 15-20 Reps", "bend rope extensions    -->3 X 15-20 Reps", "Dumbbell shrugs    -->3 X 20-30 Reps"]
        backmiddle = ["T-bar pulls    -->3 X 15-20 Reps", "One arm rowing    -->3 X 15-20 Reps", "Good morning stretches    -->3 X 30-70 Reps", "Single/Double hand rowing pulls    -->3 X 15-20 Reps"]
        backheavy = ["In/Out Bar rowing    -->3 X 20 Reps", "Bar shrugs    -->3 X 20-40 Reps", "Deadlift    -->3 X 10-20 Reps", "Lats pulldown    -->3 X 15-20 Reps"]
        return [random.choice(backwarmup), random.choice(backlight), random.choice(backmiddle), random.choice(backheavy)]
    elif muscle == 'abs':
        abslight = ["Bicycle crunches    -->3 X 20-35 Reps", "windshield wiper    -->3 X 20 Reps", "leg lifts    -->2 X 30 Reps", "Flutter kicks    -->4 X 20 Reps", "V-ups    -->2 X 20 Reps", "Russian twists    -->3 X 20-25 Reps"]
        absmiddle = ["Plank    -->3 X 3-10 mins", "Side planks    -->3 X 3-5 mins", "Reverse crunches    -->2 X 30-60 Reps", "Alternate arm-leg plank    -->3 X 20-30 Reps", "Side bend    -->2 X 60-120 Reps"]
        return [random.choice(abslight), random.choice(absmiddle), random.choice(abslight), random.choice(absmiddle)]
    elif muscle == 'cardio':
        cardmiddle = ["High knees    -->2 X 20 Reps", "Tuck jumps    -->2 X 20 Reps", "Mountain climber    -->2 X 50-80 Reps", "Steppings    -->3 X 100-200 Reps", "Jumping jacks    -->3 X 50-100 Reps", "Rope skipping    -->2 X 50-150 Reps", "Stationery bike    -->20 mins"]
        cardheavy = ["Toe touches    -->2 X 40-60 Reps", "Treadmill run    -->2 X 15-30 mins", "Cycling    -->20-40 mins", "Running    -->2 X 20 mins", "Elliptical trainer    -->2 X 15-20", "Stationery rowing    -->2 X 40-80 Reps", "Kickbacks    -->2 X 50-100 Reps"]
        return [random.choice(cardmiddle), random.choice(cardheavy), random.choice(cardheavy), random.choice(cardmiddle)]
    elif muscle == 'body weight training':
        bwmiddle = ["Side lunges    -->3 X 20 Reps", "Step ups    -->3 X 30-50 Reps", "Split squat    -->2 X 20-50 Reps", "Jump squat    -->3 X 20-50 Reps", "Burpees    -->2 X 50-100 Reps", "Glute bridge    -->2 X 50 Reps", "Lateral leg raises    -->2 X 30-40 Reps Each side"]
        bwheavy = ["Pistol squats    -->2 X 20-30 Reps", "Reverse lunges    -->3 X 20-50 Reps", "Bear crawl    -->3 X 30-50 Reps", "PLank    -->2 X 2-5 mins", "Froggers    -->3 X 20-40 Reps", "Lateral plank walks    -->3 X 5-10 mins"]
        return [random.choice(bwmiddle), random.choice(bwheavy), random.choice(bwheavy), random.choice(bwmiddle)]
    else:
        return print("Inappropriate choice.....\n")




if __name__ == '__main__':
    app.run(debug=True, port=9000)











