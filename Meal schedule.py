# Author: Ryan Bradshaw - https://www.ryanbradshaw.dev/

# TODO Allow the user to select days when they know they can't make a new meal
# TODO Write the meal plan to a file (or maybe a spreadsheet) so it can be presented better and stored for future use
# TODO Allow user to remake the meal plan if they want to at the end of the program
# TODO Move the dinner_list to a separate file

import random

# Dictionary of meals and the number of days they provide leftovers for
dinner_list = {
    "Chicken noodles": 1,
    "Chicken wrap": 2,
    "Tuna pasta mayo": 1,
    "Cottage pie": 2,
}

# https://www.bbcgoodfood.com/recipes/cottage-pie

DAYS_OF_THE_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
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
relevant_days = [None] * planner_length

# If the planner_length is > the sum of leftover meals + the number of meals in the dinner_list, exit the program
if planner_length > sum(dinner_list.values()) + len(dinner_list):
    print("---------------------------------------------")
    print("Error: Not enough meals to fill the meal plan")
    print("---------------------------------------------")
    exit()
    
# Fill meal_days with the days of the week starting from the starting day
for i in range(planner_length):
    relevant_days[i] = DAYS_OF_THE_WEEK[(starting_day - 1 + i) % 7]

# Function to choose a random meal from the dinner_list and add it to the meal_plan
def add_meal():
    meal_choice = random.choice(list(dinner_list.keys()))
    meal_plan.append(meal_choice)

# Function that handles leftover meals
def handle_leftovers():
    try:
        leftover_meals = dinner_list[meal_plan[-1]] 
    except:
        print("an error occurred")
        return
    
    for i in range(leftover_meals):
        meal_plan.append(meal_plan[-1])

    # Remove the meal from the dinner_list
    del dinner_list[meal_plan[-1]]

# Function that determines if the meal plan is full
def is_full():
    return len(meal_plan) >= planner_length

# Driver function
def generate_meal_plan():
    while (not is_full()):
        add_meal()
        handle_leftovers()
        
# Function that prints the days and meals in the meal plan
def print_meal_plan():
    print("------------------------------------")

    for i in range(planner_length):
        # If the meal has appeared before, append leftover to print string
        if meal_plan[i] in meal_plan[:i]:
            print(relevant_days[i] + ": " + meal_plan[i] + " (leftover)")
        else:
            print(relevant_days[i] + ": " + meal_plan[i])

    print("------------------------------------")

# --- Run the program ---
generate_meal_plan()
print_meal_plan()


