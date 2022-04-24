import random

while True:
  choice = ["rock", "paper", "scissor"] 
  computer = random.choice(choice)

  player = None

  while player not in choice:
    player = input("Rock, Paper or Scissor? ").lower()


  if player == computer:
    print("Computer chooses: ",computer)
    print("You choose: ",player)
    print("Tie!")
  elif player == "rock":
    if computer == "paper":
      print("Computer chooses: ",computer)
      print("You choose: ",player)
      print("You Lose!")
  elif player == "paper":
    if computer == "scissor":
      print("Computer chooses: ",computer)
      print("You choose: ",player)
      print("You Lose!")
  elif player == "scissor":
    if computer == "rock":
      print("Computer chooses: ",computer)
      print("You choose: ",player)
      print("You Lose!")
  elif player == "scissor":
    if computer == "paper":
      print("Computer chooses: ",computer)
      print("You choose: ",player)
      print("You Win!")
  elif player == "paper":
    if computer == "rock":
      print("Computer chooses: ",computer)
      print("You choose: ",player)
      print("You Win!")
  elif player == "rock":
    if computer == "scissor":
      print("Computer chooses: ",computer)
      print("You choose: ",player)
      print("You Win!")
  Play_Again = input("Want to play again? (Yes / No): ").lower()

  if Play_Again != "yes":
    break