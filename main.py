
import random



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

print("Type 0 for Rock, 1 for Paper or 2 for Scissors.")
choice = int(input("Choose your option: "))
print("You chose:", options[choice])


computer_choice = random.randint(0, 2)
computer = options[computer_choice]
print("Computer chose:", computer)

if choice == computer_choice:
    print("It's a draw.")
elif (choice == 0 and computer_choice == 2) or \
    (choice == 2 and computer_choice == 1) or \
    (choice == 1 and computer_choice == 0):
    print("You win.")
else:
    print("You lose.")