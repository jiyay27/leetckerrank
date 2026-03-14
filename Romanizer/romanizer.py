#!/bin/python3
import math
import os
import random
import re
import sys

def romanizer(numbers):
    roman_numerals = {
        1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
        6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
        40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
        500: 'D', 900: 'CM', 1000: 'M'
    }

    ans = []

    for number in numbers:
        number_roman = ''
        for value in sorted(roman_numerals.keys(), reverse=True):
            while number >= value:
                number_roman += roman_numerals[value]
                number -= value

        ans.append(number_roman)

    return ans

if __name__ == '__main__':

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = romanizer(numbers)

    print('\n'.join(result))
