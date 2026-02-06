# Number Guess Project

import random

randomNumber = random.randrange(1, 11)
guess = 0
guess_history = []
used_numbers = []
while guess != randomNumber:
    guess = int(input("Guess: "))
    if guess > randomNumber:
        print("Your guess is GREATER than the number")
        guess_history.append(guess)
    elif guess < randomNumber:
        print("Your guess is LESS than the number")
        guess_history.append(guess)
    used_numbers.append(guess)
    print(f"Used numbers: {used_numbers}")

print(f"your guess is correctamundo, the number was {randomNumber}")
print("Guess history:")
for i in guess_history:
    print(f"    Incorrect guess: {i}")