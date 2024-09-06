from collections import *
def pluck(arr):
    # Your code here!
    even, index = min(filter(lambda x: x % 2 == 0, arr), key=lambda x: x)
    return [even, index] if even else []