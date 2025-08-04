"""print("Hello, welcome to Kay's CoffeeShop!")

name = input("What is your name? ")

#this is for Ben
if name == "Ben" or name == "Patricia":
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "Yes" and good_deeds < 4:
                        
      print("You're not allowed in this bussiness, " + name + ".")
      print(input("Press the ENTER key to exit."))
      exit()
    else:
        print("Oh, so you're one of the good ones, come in.")
#this is if the rest of the normal code

menu = "Black Coffee ($3), Iced Coffee ($2.23), Expresso ($4), Latte ($5),\n Frappuccino ($3.44)\n"
print("\nOk " + name + ", let us show you our menu.\n")
print(menu)
print(name + ", what would you like from our menu? (above)\n")
order = input()
price = 6 + .12
if order == "Black Coffee":
    price = 3
elif order == "Iced Coffee":
    price = 2.23
elif order == "Expresso":
    price = 4
elif order == "Latte":
    price = 5
elif order == "Frappuccino":
    price = 3.44
quantity = input("\nHow many coffees would you like?\n")
total = price * int(quantity)
    
print("\nGot it, your total will be $" + str(total) ,"dollars after tax.")
print("\nYour order will be ready in a few minutes.")




camping_stuff = ["tent", "sleeping bags", "water",
                 "coffee", "knife", "flashlight"]

camp_site = ["Crystal Lake", 404, 89.4, True]

camping_stuff.insert(3, "boots")

camping_stuff.insert(0, "toiletpaper")

#camping_stuff.clear()

camping_stuff.remove("water")
camping_stuff.remove("knife")

print("This item was just deleted: " + camping_stuff.pop(0))

print(camping_stuff)


import random
from sty import fg

def generateRGB():
    red = random.randint(0,256)
    green = random.randint(0,256)
    blue = random.randint(0,256)
    return red, green, blue

def generateColour(red, green, blue):
    return fg(red, green, blue)

red, green, blue = generateRGB()
colour = generateColour(red, green, blue)
print(colour,"I am testing this")



class Guitar:
    def __init__(self, n_strings=6):
        self.n_strings = n_strings
        self.play()
    def play(self):
        print("pam pam")

class BassGuitar(Guitar):
    pass

class ElectricGuitar(Guitar):
    def __init__(self):
        super().__init__()
        self.n_strings = 8
    def playLouder(self):
        print("pamm plamm".upper())


print(BassGuitar(4).n_strings)


#DATES
from datetime import datetime

# Get current date and time
now = datetime.now()

# Format the current date and time
formatted_date_time = now.strftime("%A, %B %dth, %Y. \nThe time is %I:%M:%S %p")

# Print the formatted date and time
print("Hello, today is:", formatted_date_time, "\n\nHave a blessed rest of your day!")

import numpy as np

# Create a 30x5 NumPy array filled with random numbers
data = np.random.rand(30, 5)

# Print the data
print(data)"""


print("print", "low")
