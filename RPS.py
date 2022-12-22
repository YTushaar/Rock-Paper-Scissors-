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

import random

imag = [rock, paper, scissors]
a = int(input("enter 0 for rock, 1 for paper, 2 for scissors "))
b = random.randint(1, 3)
print(imag[a])
print(imag[b])
if (a == b):
    print("Draw")
elif a == 0 and b == 1:
    print("computer wins")
elif a == 0 and b == 2:
    print("user wins")
elif a == 1 and b == 2:
    print("computer wins")
elif a == 1 and b == 0:
    print("user wins")
elif a == 2 and b == 0:
    print("computer wins")
elif a == 2 and b == 1:
    print("user wins")
