#!/usr/bin/env python3
# Created by: Shem
# Created on: 2025/11/27
# This program prints the integers from 1000 to 2000,
# displaying five numbers per line.


def main():
    for year in range(1000, 2001, 1):
        print(year, end=" ")

        # Print a new line after every 5 numbers
        if year % 5 == 0:
            print()  # Move to the next line

    # Print thank you message after all numbers are printed
    print("\nThank you for playing")
    print(" /\\_/\\  ")
    print("( ^_^ )")
    print(" > ^ < ")


if __name__ == "__main__":
    main()
