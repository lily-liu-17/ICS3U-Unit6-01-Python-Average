#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program finds the averae of 10 random numbers

import random


def main():
    # This program finds the averae of 10 random numbers
    number_list = []

    print("Starting ...")

    for loop_counter in range(0, 10):
        random_number = random.randint(1, 100)
        number_list.append(random_number)

        print("The random number is : {0}".format(random_number))

    average = sum(number_list) / len(number_list)

    print("")
    print("The average is {0}".format(average))

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
