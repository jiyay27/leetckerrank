import math
import os
import random
import re
import sys

def getOneBits(n):
    ans = []
    count = 0
    pos = 0

    binary_string = bin(n)
    binary_array = list(binary_string)
    binary_array = binary_array[2:]

    for x in binary_array:
        pos += 1
        if x == '1':
            count += 1
            ans.append(pos)

    ans.insert(0, count)

    return ans

if __name__ == '__main__':
    n = int(input().strip())

    result = getOneBits(n)

    print(result)
