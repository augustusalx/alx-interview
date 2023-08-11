#!/usr/bin/python3
"""
The minimum Operations
Given num n, write a method which calculates the fewest number of operations
needed to result exactly in n H characters in a file
Prototype: def minOperations(n)

"""


def minOperations(n):
    """
    Function minOperations
    Returns an integer
    """
    result = 0
    x = 2
    while n > 1:
        while n % x == 0:
            result += x
            n /= x
        x += 1
    return result
