import random

secret = random.randint(1, 20) # gets a random value between 1 and 20

while True:
    user_guess = int(input("Enter a number between 1 and 20: "))
    
    if user_guess < secret :
        print("Too low, try again!")
    elif user_guess > secret :
        print("Too high, try again!")
    else :
        print(f"🔥 Correct, the number was {secret}")
        break

# Assignment on Number Guessing Game
# ==================================
# 1. Upgrade the project