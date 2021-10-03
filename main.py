import random

while True:
    my_answer = input("Choose: rock, paper or scissors: ")
    my_answer = my_answer.lower()

    if my_answer == "quit":
        break
    if my_answer != "rock" and my_answer !="paper" and my_answer !="scissors":
        print ("Please choose either rock, paper or scissors")
        continue

    computer_answer = random.choice(["rock", "paper", "scissors"])
    print (f"Computer choose: {computer_answer}")

    if my_answer == computer_answer:
        print ("It is a tied game")
        continue
    elif my_answer == "paper" and computer_answer == "rock":
        print ("You win")
        break
    elif my_answer == "rock" and computer_answer == "scissors":
        print ("You win")
        break
    elif my_answer == "scissors" and computer_answer == "paper":
        print ("You win")
        break
    else:
        print ("Computer wins")
