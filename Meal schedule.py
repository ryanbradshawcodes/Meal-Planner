# Author: Ryan Bradshaw - https://www.ryanbradshaw.dev/

# ! Entering too few meals (planner_length) will result in an error
# TODO Allow the user to select days when they know they can't make a new meal

import random

# Dictionary of meals and the number of days they provide leftovers for
dinner_list = {
    "Chicken noodles": 1,
    "Chicken wrap": 2,
    "Tuna pasta mayo": 1,
    "Cottage pie": 2,
}

#https://www.bbcgoodfood.com/recipes/cottage-pie

meal_plan = []

print("----------------------------")
print("Welcome to the Meal Planner!")
print("----------------------------")

print("Please enter the starting day: \n")
print("1. Monday \t 2. Tuesday\n")
print("3. Wednesday \t 4. Thursday\n")
print("5. Friday \t 6. Saturday\n")
print("\t 7. Sunday\n")

starting_day = int(input("Enter the starting day: "))
planner_length = int(input("Enter how many days you want to plan for: "))

DAYS_OF_THE_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
relevant_days = [None] * planner_length

# Fill meal_days with the days of the week starting from the starting day
for i in range(planner_length):
    relevant_days[i] = DAYS_OF_THE_WEEK[(starting_day - 1 + i) % 7]

# Function to choose a random meal from the dinner_list and add it to the meal_plan
def add_meal():
    try:
        meal_choice = random.choice(list(dinner_list.keys()))
        meal_plan.append(meal_choice)
    except:
        meal_plan.append("No meal")
        return

# Function that handles leftover meals
def handle_leftovers():
    try:
        leftover_meals = dinner_list[meal_plan[-1]] 
    except:
        return
    
    for i in range(leftover_meals):
        meal_plan.append(meal_plan[-1])

    # Remove the meal from the dinner_list
    del dinner_list[meal_plan[-1]]

# Function that determines if the meal plan is full
def is_full():
    if len(meal_plan) == planner_length:
        return True
    else:
        return False

# Driver function
def generate_meal_plan():
    while (not is_full()):
        try:
            add_meal()
            handle_leftovers()
        except:
            return
        
# Function that prints the days and meals in the meal plan
def print_meal_plan():
    for i in range(planner_length):
        # If the meal has appeared before, append leftover to print string
        if meal_plan[i] in meal_plan[:i]:
            print(relevant_days[i] + ": " + meal_plan[i] + " (leftover)")
        else:
            print(relevant_days[i] + ": " + meal_plan[i])

# ---------------------
generate_meal_plan()
print_meal_plan()


