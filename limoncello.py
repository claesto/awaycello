#!/usr/bin/env python3

def calculate_limoncello_recipe(alcohol_volume):
    # original recipe
    original_alcohol_volume = 1000  # ml
    original_water_volume = 1500    # ml
    original_sugar_weight = 700     # grams

    # ratios
    water_ratio = original_water_volume / original_alcohol_volume
    sugar_ratio = original_sugar_weight / original_alcohol_volume

    # calculate proportions for the given alcohol volume
    water_volume = water_ratio * alcohol_volume
    sugar_weight = sugar_ratio * alcohol_volume

    output = """
    ┏━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ 🍋 LIMONCELLO RECIPE ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━┛

    ✧ Alcohol:\t{}ml
    ✧ Water:\t{}ml
    ✧ Sugar:\t{}gr
    """.format(alcohol_volume, int(water_volume), int(sugar_weight))

    print(output)

if __name__ == "__main__":
    alcohol_volume = int(input("Enter the volume of alcohol (in ml): "))

    # Calculate and print the recipe
    calculate_limoncello_recipe(alcohol_volume)