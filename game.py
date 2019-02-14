'''
    Author: Kavinsan Thavanesan
    Application challenge for the position of Capital Market Developer
'''

import random;

def game(): #Main Game
    compOption = random.randint(1,3)
    

    print("Playing Rock, Paper, Scissors!\n Enter the following choices or representing option!\n 1. rock \n 2. paper \n 3. scissors")

    valid = False
    option = ""

    while(not valid):
        option = input("> ").lower()
        option = inputParser(option)

        if(option == 0):
            print("The option you entered is not valid! Try again")
            valid = False
            continue

        valid = True

    winner(option, compOption)

def winner(option, compOption): #Determine winner

    options = ["Rock", "Paper","Scissors"]

    print(f"Computer: I choose {options[compOption - 1]}!!")

    if(option == compOption):
        print(f"Its a draw! Both players have chosen {options[option - 1]}")
    elif (option == 1): #Player chose Rock

        if(compOption == 2): #Computer chose Paper
            print(f"{options[compOption - 1]} covers {options[option - 1]} you lose :(")
        elif(compOption == 3): #Computer chose Scissor
            print(f"{options[option - 1]} crushes {options[compOption - 1]} you win!")

    elif (option == 2): #Player chose Paper
        
        if(compOption == 1): #Computer chose Rock
            print(f"{options[option - 1]} covers {options[compOption - 1]} you win!")
        elif(compOption == 3): #Computer chose Scissor
            print(f"{options[compOption - 1]} cuts {options[option - 1]} you lose :(")

    elif (option == 3): #Player chose Scissor
        
        if(compOption == 1): #Computer chose Rock
            print(f"{options[compOption - 1]} crushes {options[option - 1]} you lose :(")
        elif(compOption == 2): #Computer chose Paper
            print(f"{options[option - 1]} cuts {options[compOption - 1]} you win!")

def inputParser(option): #Interpret user option


    if(option == "1") | (option == "rock"): #Option Rock
        return 1 
    elif(option == "2") | (option == "paper"): #Option Paper
        return 2
    elif(option == "3") | (option == "scissors"): #Option Scissors
        return 3
    else:
        return 0 #Return 0 if the option is invalid

def main():

    while(True):
        game()
        option = input("Type 'Y' to play again: \n> ").lower()
        if(option != 'y'):
            print("Thanks for playing!")
            break

main()