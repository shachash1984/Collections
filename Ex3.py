#!/usr/bin/python

var = input("Please enter an integer: ")

if var.isdecimal():
    num = int(var)
    for i in range(num, -1, -2):
        print(i)
    """
        while num >= 0:
        print(num)
        num -= 2
    """

else:
    print("Error: only integer values are acceptable")
    exit(1)

