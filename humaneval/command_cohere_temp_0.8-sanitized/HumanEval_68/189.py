from collections import *
def pluck(arr):
    # Your code here!
    even, index = min(zip(arr, range(len(arr))), key=lambda x: x if x[0] % 2 == 0 else float('inf'))
    return [even[0], index] if even != float('-inf') else []