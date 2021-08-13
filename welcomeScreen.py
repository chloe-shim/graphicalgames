import pygame, random, time

username = input("First, enter your name: ")

def welcomeScreen():
    print(f"Welcome to the game {username}, we're so happy to see you here. ")
    print()
    print("Welcome to base camp, ahead lies a vital decision. ")
    print()
    print("You can choose either the jungle tent or the space tent... choose wisely. ")
    print()
    print("You will have to win the game to recieve the prize, you will need to score 25. ")
    print()
    tentChoice = input("Input 'A' for jungle and 'B' for space. ")

    if tentChoice.upper() == "A":
        jungle_tent()
    elif tentChoice.upper() == "B":
        space_tent()
    else:
        print("Invalid input. ")
        welcomeScreen()

def jungle_tent():
    print(f"Welcome to the jungle tent explorer {username}, with the help of Sammy the Snake we will save the jungle. ")
    print("\nHelp Sammy the Snake get 25 fruits in order to save the jungle. ")
    ready = input("\nReady? Type Y or N: ")
    ready_jungle(ready)

def ready_space(answer):
    if answer.upper() == "Y":
        import spaceInvaders
    if answer.upper() == "N":
        answer2 = input("\nOk, just type Y when you are ready to launch!")
        ready_space(answer2)
    else:
        print("Go back and read the instructions again...")
        welcomeScreen()

def ready_jungle(answer):
    if answer.upper() == "Y":
        import snakeGame
    if answer.upper() == "N":
        answer2 = input("\nOk, just type Y when you are ready to explore!")
        ready_jungle(answer2)
    else:
        print("Go back and read the instructions again...")
        welcomeScreen()

def space_tent():
    print(f"Welcome to the space tent astronaut {username}, with the help of our cool teach we will save the world. ")
    print("\nHelp the astronauts kill 25 aliens in order to save the world. ")
    ready = input("\nReady? Type Y or N: ")
    ready_space(ready)

welcomeScreen()