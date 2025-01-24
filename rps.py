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

game_images=[rock,paper,scissors]

player=int(input("What do you choose? Type 0 for Rock, 1 for paper, 2 for scissors\n"))
if player>=0 and player<=2:
    print(game_images[player])


computer=random.randint(0,2)
print("Computer chose:")

print(game_images[computer])

if player>=3 or player<0:
    print("You typed an invalid number. YOU LOSE!!!")
elif player==0 and computer==2:
    print("YOU WIN!!!")
elif computer==0 and player==2:
    print("YOU LOSE!!!")
elif computer>player:
    print("YOU LOSE!!!")
elif player>computer:
    print("YOU WIN!!!")
elif computer==player:
    print("ITS A DRAW!!!")

elif player>=3 or player<0:
    print("You typed an invalid number. YOU LOSE!!!")