import json
from datetime import datetime

class Workout:
    def __init__(self, date: str, workout_type: str, duration: int, calories_burned: int):
        self.date = date
        self.workout_type = workout_type
        self.duration = duration  # in minutes
        self.calories_burned = calories_burned

    def __str__(self):
        return (f"Date: {self.date}, Type: {self.workout_type}, Duration: {self.duration} min, "
                f"Calories Burned: {self.calories_burned} kcal")

class FitnessTracker:
    def __init__(self, filename: str = "workout_data.json"):
        self.filename = filename
        self.workouts = []
        self.load_data()

    def add_workout(self, workout_type: str, duration: int, calories_burned: int):
        date = datetime.now().strftime("%Y-%m-%d")
        workout = Workout(date, workout_type, duration, calories_burned)
        self.workouts.append(workout)
        print("Workout added successfully!")

    def view_workouts(self):
        if not self.workouts:
            print("No workouts recorded yet.")
            return

        print("\n--- Workout History ---")
        for i, workout in enumerate(self.workouts, 1):
            print(f"{i}. {workout}")

    def view_progress_summary(self):
        if not self.workouts:
            print("No data available for progress summary.")
            return
        total_duration = sum(workout.duration for workout in self.workouts)
        total_calories = sum(workout.calories_burned for workout in self.workouts)
        total_workouts = len(self.workouts)
        print("\n--- Progress Summary ---")
        print(f"Total Workouts: {total_workouts}")
        print(f"Total Duration: {total_duration} minutes")
        print(f"Total Calories Burned: {total_calories} kcal")
    def save_data(self):
        with open(self.filename, "w") as file:
            json_data = [workout.__dict__ for workout in self.workouts]
            json.dump(json_data, file)
        print("Data saved successfully!")
    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                json_data = json.load(file)
                self.workouts = [Workout(**data) for data in json_data]
        except FileNotFoundError:
            self.workouts = []
    def run(self):
        while True:
            print("\n--- Personal Fitness Tracker ---")
            print("1. Add Workout")
            print("2. View Workouts")
            print("3. View Progress Summary")
            print("4. Save and Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                workout_type = input("Enter workout type (e.g., Running, Yoga): ")
                duration = int(input("Enter duration (in minutes): "))
                calories_burned = int(input("Enter calories burned: "))
                self.add_workout(workout_type, duration, calories_burned)
            elif choice == "2":
                self.view_workouts()
            elif choice == "3":
                self.view_progress_summary()
            elif choice == "4":
                self.save_data()
                print("Exiting the tracker. Stay fit!")
                break
            else:
                print("Invalid choice. Please try again.")
if __name__ == "__main__":
    tracker = FitnessTracker()
    tracker.run()