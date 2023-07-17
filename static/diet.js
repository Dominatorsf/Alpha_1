//function submitForm() {
//    var dietPlan = document.querySelector('input[name="dietPlan"]:checked').value;
//
//    if (dietPlan === "weightGain") {
//        // Code for weight gain diet plan
//        console.log("Weight Gain Diet Plan");
//
//        // Display recommended meals for weight gain
//        var recommendedMeals = ["Breakfast: Protein smoothie with oats and fruits",
//                                "Lunch: Grilled chicken with brown rice and vegetables",
//                                "Snack: Almonds and Greek yogurt",
//                                "Dinner: Salmon with quinoa and roasted vegetables"];
//        console.log("Recommended Meals for Weight Gain:");
//        for (var i = 0; i < recommendedMeals.length; i++) {
//            console.log(recommendedMeals[i]);
//        }
//
//        // Display workout recommendations for weight gain
//        var workoutRecommendations = ["Strength training exercises targeting major muscle groups",
//                                      "Compound movements like squats, deadlifts, and bench press",
//                                      "Aim for progressive overload and increase weights over time"];
//        console.log("Workout Recommendations for Weight Gain:");
//        for (var j = 0; j < workoutRecommendations.length; j++) {
//            console.log(workoutRecommendations[j]);
//        }
//    } else if (dietPlan === "weightLoss") {
//        // Code for weight loss diet plan
//        console.log("Weight Loss Diet Plan");
//
//        // Display recommended meals for weight loss
//        var recommendedMeals = ["Breakfast: Avocado toast with poached eggs",
//                                "Lunch: Grilled chicken salad with mixed greens and vinaigrette",
//                                "Snack: Apple slices with almond butter",
//                                "Dinner: Baked salmon with steamed vegetables"];
//        console.log("Recommended Meals for Weight Loss:");
//        for (var i = 0; i < recommendedMeals.length; i++) {
//            console.log(recommendedMeals[i]);
//        }
//
//        // Display workout recommendations for weight loss
//        var workoutRecommendations = ["Cardio exercises like running, cycling, or swimming",
//                                      "High-intensity interval training (HIIT) workouts",
//                                      "Incorporate strength training to maintain muscle mass"];
//        console.log("Workout Recommendations for Weight Loss:");
//        for (var j = 0; j < workoutRecommendations.length; j++) {
//            console.log(workoutRecommendations[j]);
//        }
//    } else {
//        // Handle case when no diet plan is selected
//        console.log("Please select a diet plan");
//    }
//}


//
//function submitForm() {
//    var dietPlan = document.querySelector('input[name="dietPlan"]:checked').value;
//
//    if (dietPlan === "weightGain") {
//        // Code for weight gain diet plan
//        console.log("Weight Gain Diet Plan");
//
//        // Display recommended meals for weight gain
//        var recommendedMeals = ["Breakfast: Protein smoothie with oats and fruits",
//                                "Lunch: Grilled chicken with brown rice and vegetables",
//                                "Snack: Almonds and Greek yogurt",
//                                "Dinner: Salmon with quinoa and roasted vegetables"];
//        document.getElementById("recommendedMeals").textContent = "Recommended Meals for Weight Gain:\n" + recommendedMeals.join("\n");
//
//        // Display workout recommendations for weight gain
//        var workoutRecommendations = ["Strength training exercises targeting major muscle groups",
//                                      "Compound movements like squats, deadlifts, and bench press",
//                                      "Aim for progressive overload and increase weights over time"];
//        document.getElementById("workoutRecommendations").textContent = "Workout Recommendations for Weight Gain:\n" + workoutRecommendations.join("\n");
//    } else if (dietPlan === "weightLoss") {
//        // Code for weight loss diet plan
//        console.log("Weight Loss Diet Plan");
//
//        // Display recommended meals for weight loss
//        var recommendedMeals = ["Breakfast: Avocado toast with poached eggs",
//                                "Lunch: Grilled chicken salad with mixed greens and vinaigrette",
//                                "Snack: Apple slices with almond butter",
//                                "Dinner: Baked salmon with steamed vegetables"];
//        document.getElementById("recommendedMeals").textContent = "Recommended Meals for Weight Loss:\n" + recommendedMeals.join("\n");
//
//        // Display workout recommendations for weight loss
//        var workoutRecommendations = ["Cardio exercises like running, cycling, or swimming",
//                                      "High-intensity interval training (HIIT) workouts",
//                                      "Incorporate strength training to maintain muscle mass"];
//        document.getElementById("workoutRecommendations").textContent = "Workout Recommendations for Weight Loss:\n" + workoutRecommendations.join("\n");
//    } else {
//        // Handle case when no diet plan is selected
//        console.log("Please select a diet plan");
//    }
//
//    // Show the diet plan display section
//    document.getElementById("dietPlanDisplay").style.display = "block";
//}