import random

name = input('What is you name? ')

print('Best of luck', name)

words = ['apple', 'mouse', 'deer', 'lion', 'science', 'math', 'jump', 'snow', 'star', 'machine', 'random']

word = random.choice(words)
print('Guess the letters')

guesses = ''
turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_')
            failed += 1
    if failed == 0:
        print("You Won")
        print('The word is: ', word)
        break
    print()
    guess = input('guess a character:')
    guesses += guess

    if guess not in word:
        turns -= 1
        print('Wrong')
        print('You have', +turns, 'more guessess')

        if turns == 0:
            print('You lost')