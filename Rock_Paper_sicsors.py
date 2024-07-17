# if >>(rock)*(paper) = paper wins
# if >>(rock)*(scissor) = rock wins
# if >>(paper)*(scissor) = scissors


import random
option=("rock","paper","scissors")

running = True

while running:
    player=None
    computer=random.choice(option)

    while player not in option:
        player = input("Enter your choice(rock,paper,scissors): ")

    print(f"player:{player}")
    print(f"computer:{computer}")

    if player== computer:
        print("it is tie!")
    elif player== "rock" and computer=="scissors":
        print("you win!")
    elif player == "paper" and computer == "rock":
        print("you win!")
    elif player == "scissors" and computer == "paper":
        print("you win!")
    else :
        print("you lose!")
    play_again = input("you want play again? (yes/no): ").lower()
    if not play_again == "yes":
        running=False



print("Thanks for playing!")