# system takes indexed values and prints it to show how the person felt during their previous game session with that game.
# after that, it shows a graph showing their feeling levels over time with the game - still working on this.
# finally, it asks if you wish to continue with your choice or not. You can say yes or no. The system will close for either decision.


# Import necessary files

import matplotlib.pyplot as plt
import time
import numpy as np
import sys

# Project simulates an experiment to see chances and choices made by an individual.

#Session 1 readings

# def ChoiceInput():
Choice_thought = int(input("thought index: "))
choice_fun = int(input("fun index: "))

# ChoiceInput()

Choice_thought2 = int(input("thought index: "))
choice_fun2 = int(input("fun index: "))

SpideyMilesMorales = {
    # Everything is out of a 0-100 scale.
    "Thought": Choice_thought,
    "Fun": choice_fun,
    # "Creativity": 85,
    # "Happiness": 95,
}

Nba2k24 = {
    # Everything is out of a 0-100 scale
    "Thought": Choice_thought2,
    "Fun": choice_fun2,
    # "Creativity": 87,
    # "Happiness": 90,
}


def ChoiceMaker():
  # look for initial game choice and show stimulation values.
    GameChoice = input("Spider-Man or NBA2K24: ")
    if GameChoice == "Spider-Man" or "Spider-man":
        print(GameChoice + " has been chosen!")
        time.sleep(0.2)
        print(SpideyMilesMorales)
    elif GameChoice == "NBA2k24" or "2k24":
        print(GameChoice + " has been chosen!")
        time.sleep(0.2)
        print(Nba2k24)
    else:
        pass

#define function to plot graph of values
  
    def Session1():
        plt.xlabel("Time")
        plt.ylabel("Feeling Level")
        plt.title("Feeling level index")
        x = np.linspace(0,100,2)
        y = [0,100]

        plt.plot(x,y, color="blue")
        plt.show()

  # define the function
  
    Session1()

  # system will ask if you wish to continue with the choice you made earlier.
  
    ChoiceContinue = input("Do you wish to continue? ")
    if ChoiceContinue == "yes" or "y":
        sys.exit()
    elif ChoiceContinue == "no" or "n":
        sys.exit()

# define the function

ChoiceMaker()










