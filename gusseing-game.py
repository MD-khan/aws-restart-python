#!/usr/bin/env python

import random
"""
    This scriptt asks the user to correctly guess a number.
    User only allow to guess three times.
    Each try script will generate random number
    Each try, user will see both of his/her guessed number and the scriptt generated number
    if user guessed number mached with scriptt generated number
    Congrats user 
    If user cant not  guess the number with three try
    show message try again
    
"""

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")


isGuessRight = False

user_try_count = 0
while isGuessRight == False:
    if user_try_count == 3:
        print("You have reached the maximum number of try\nPlease try again!")
        exit()
    guess = input("Guess a number between 1 and 10: ")
    number = random.randint(1, 10)
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        user_try_count += 1
        print("You have tried {} times".format(user_try_count))
        isGuessRight = True
    else:
        user_try_count += 1
        print("You have tried {} times".format(user_try_count))
        print("You guessed {}.\nSorry, that isn\'t it\nThe actual number was {}\n".format(
            guess, number))
