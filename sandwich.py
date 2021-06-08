from typing import OrderedDict
import pyinputplus as pyip

sandwich = [] #for the order
cost = 0 #adds up the cost

# asks what bread type
bread = pyip.inputMenu((["wheat bread","white bread","sourdough bread"]),prompt="What bread type: \n", numbered=True)
# for different cost
if bread == "wheat" or bread == "white" :
    cost += 1.5
else:
    cost += 2
# adds to the order
sandwich.append(bread)

# asks what meat type
meat = pyip.inputMenu((["chicken", "turkey", "tofu"]), prompt="What meat type: \n", numbered=True)
# for the diffferent cost of meat
if meat == "chicken" or meat == "turkey" :
    cost += 2.5
else:
    cost += 2
# adds to the order
sandwich.append(meat)

# checks if they want cheese
cheeseCheck = pyip.inputYesNo(prompt="Do you want cheese?\n")
if cheeseCheck == 'yes' :
    # asks what type of cheese
    cheese = pyip.inputMenu((["cheddar","swiss","mozzarella"]),prompt="What cheese type:\n",numbered=True)
    # for different cost of cheese
    if cheese == "cheddar" or cheese == "swiss" :
        cost += 1.25
    else:
        cost += 1.75
    # adds to order
    sandwich.append(cheese)

# checks if they want extras
extraCheck = pyip.inputYesNo(prompt="Do you want mayo, mustard, lettuce or tomato?\n")
if extraCheck == 'yes' :
    # asks which extra
    extra = pyip.inputMenu((["mayo","mustard","lettuce","tomato"]),prompt="What extra would you like?\n", numbered=True)
    # adds to cost
    cost+= 1
    # adds to order
    sandwich.append(extra)

# asks how many sandwiches
many = pyip.inputInt(prompt="How many sandwiches would you like?\n", min=1)

# multiples by how many sandwiches
cost*= many
# formats to display two decimal places
cost = "%.2f" % cost
# pus order into a string
order = " ".join(sandwich)
# for wording purposes
if many >1 :
    sandwichCheck = "sandwiches"
else:
    sandwichCheck = "sandwich"
# print nicely
print(f"You ordered {many} {sandwichCheck}")
print(f"with {order}")
print(f"The total cost is {cost}")



