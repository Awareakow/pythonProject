# This is a python game for Rock paper scissors.
# Date: Dec 31 2022
# By: Derek Xiao
# Version V1.0
from random import randint
R = 'Rock'
P = 'Paper'
S = 'Scissors'
t = ["Rock", "Paper", "Scissors", "R", "P", "S"]
computer = t[randint(0,2)]
player = False
while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
        #Line filler
        #Line filler



    player = False
    computer = t[randint(0,2)]





