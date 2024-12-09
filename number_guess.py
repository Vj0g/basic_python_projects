import random

print('Hi! Welcome, This is number guessing game. You got 5 chances')

guess_this_number = random.randrange(100)

chances = 5

guess_count = 0

while guess_count < chances:
    guess_count += 1
    my_guess = int(input('Please enter your guess :'))

    if my_guess == guess_this_number:
        print(f'The number is {guess_this_number} and you guess it !! in the {guess_count} attempt')
        break
    elif guess_count>=chances and my_guess != guess_this_number:
        print(f"Sorry, The number is {guess_this_number} better luck next time")
    elif my_guess > guess_this_number:
        print('Your guess is higher')
    elif my_guess< guess_this_number:
        print('Your guess is lower')