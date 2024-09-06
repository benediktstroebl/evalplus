from collections import *
def pluck(arr):
    # Your code here!
    even, index = min(zip(filter(lambda x: x % 2 == 0, arr), range(len(arr))))
    return [even, index] if even != NULL else []