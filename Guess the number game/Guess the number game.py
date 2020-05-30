

from random import sample, shuffle

digits = 2
guesses = 10

print('Hi there! I am thinking of a', digits, 'digit number.')
print('Try to guess what it is.')
print('Here are some clues:')
print('When I say:    That means:')
print('  orange         One digit is correct but in the wrong position.')
print('  green          One digit is correct and in the right position.')
print('  red            No digit is correct.')
print('\nThere are no repeated digits in the number.')

# Creating a random number.

letters = sample('0123456789', digits)

if letters[0] == '0':
    letters.reverse()

number = ''.join(letters)

print('\nI have thought up a number.')
print('You have', guesses, 'guesses to get it. \n')

counter = 1

while True:
    print('\nGuess #', counter)
    guess = input()

    if len(guess) != digits:
        print('Wrong number of digits. Try again!')
        continue

    # Creating the clues section.

    clues = []

    for index in range(digits):
        if guess[index] == number[index]:
            clues.append('green')
        elif guess[index] in number:
            clues.append('orange')

    shuffle(clues)

    if len(clues) == 0:
        print('red')
    else:
        print(' '.join(clues))

    counter += 1

    if guess == number:
        print('\nWooh! You got the correct mumber!')
        break

    if counter > guesses:
        print('POOR KID! You ran out of guesses. The answer was', number)
        break
