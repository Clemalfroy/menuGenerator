from plat import Plat
import json
import random

def loadMeal():
    meals = []
    menus = json.load(open("menu.json"))
    for menu in menus:
        meal = Plat(menu["name"], menu["fitness"])
        meals.append(meal)
    return meals

def findMenu(meals):
    numberMeals = len(meals)
    firstMeal = meals[random.randint(0, numberMeals - 1)]
    firstMeal.used = True 
    found = False
    while not found:
        secondMeal = meals[random.randint(0, numberMeals - 1)]
        if not secondMeal.used:
            secondMeal.used = True
            if firstMeal.fitness + secondMeal.fitness == 10:
                found = True
    return firstMeal, secondMeal



def main():
    meals = loadMeal()
    menu = findMenu(meals)
    print("Plat 1 : {} \nPlat 2 : {}".format(menu[0].name, menu[1].name))
    
if __name__ == "__main__":
    main()
