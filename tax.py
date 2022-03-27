#!/usr/bin/env python3
# Created By: Paterry Baptichon junior
# Date: March 27 2022
# This program asks the user for the subtotal and the tax
# percentage. It then calculates and displays the HST
# and the total.


import constants


def main():
    # get user input
    print("This program will calculate the taxes in New Brunswick")
    subtotal = float(input("Enter subtotal: $"))
    
    # calculate the tax amount and the total with tax
    tax = subtotal * constants.TAX_RATE_NB / 100
    total = subtotal + tax

    # display the tax amount and the total with tax
    print("")
    print("You entered a subtotal of ${:.2f}".format(subtotal))
    print("The HST is ${0:.2f} and the total is ${1:.2f}".format(tax, total))


if __name__ == "__main__":
    main()