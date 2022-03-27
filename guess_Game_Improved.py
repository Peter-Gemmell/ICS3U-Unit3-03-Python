#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on March 2022
# This program checks to see if the number guessed is the random number

import random


def main():
    # this program checks to see if the number guessed is the random number

    # input
    guess_Number = int(input("Enter a number(between 0-9): "))
    print("")
    mystery_Number = random.randint(0, 9)  # a number between 0 and 9

    # process & output
    if guess_Number == mystery_Number:
        print("You guessed correctly!")
        print("\nDone.")
    else:
        print("You guessed incorrectly. Try again.")
        print("")
        print("The correct number was: {} ".format(mystery_Number))
        print("\nDone.")


if __name__ == "__main__":
    main()
