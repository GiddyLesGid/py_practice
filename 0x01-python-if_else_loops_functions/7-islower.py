#!/usr/bin/python3

"""
A function that checks for lowercase character
"""


def islower(self, c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
