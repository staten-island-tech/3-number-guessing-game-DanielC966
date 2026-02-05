# Number Guess Project

import random

randomNumber = random.randrange(1, 11)
guess = 0
guess_history = []
while guess != randomNumber:
    guess = int(input("Guess: "))
    if guess > randomNumber:
        print("Your guess is GREATER than the number")
        guess_history.append(guess)
    elif guess < randomNumber:
        print("Your guess is LESS than the number")
        guess_history.append(guess)

print(f"your guess is correctamundo, the number was {randomNumber}")
print("Guess history: \n")
for i in guess_history:
    print(guess_history[i])