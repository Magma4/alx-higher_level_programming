#!/usr/bin/python3
"""class Square"""


class Square:
    """square class with it's size and proper validation"""

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """calculates and returns area of a square"""

        return self.__size ** 2 
