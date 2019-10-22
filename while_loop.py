#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: October 2019
# This program uses a while loop


def main():
    # this function uses a while loop
    loop_counter = 1
    some_sum = 0

    print("Find the sum of a number.")

    # input
    some_num_string = input("Enter a positive integer: ")
    print("")

    # process & output
    try:
        some_num = int(some_num_string)
        while loop_counter <= some_num:
            print("{0}".format(loop_counter))
            some_sum = loop_counter + some_sum
            loop_counter += 1

        print("The sum of your number is {0}.".format(some_sum))
    except Exception:
        print("Wrong input. Try again.")


if __name__ == "__main__":
    main()
