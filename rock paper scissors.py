import random

options = ["rock","paper","scissors"]
computerschoice = random.choice(options)
playerchoice = input("enter rock paper scissors ")
if playerchoice == computerschoice:
    print("it is a tie")

if computerschoice == "rock" and playerchoice == "paper":
    print("you win")
if computerschoice == "paper" and playerchoice == "scissors":
    print("you win")
if computerschoice == "scissors" and playerchoice == "rock":
    print("you win")






































































































