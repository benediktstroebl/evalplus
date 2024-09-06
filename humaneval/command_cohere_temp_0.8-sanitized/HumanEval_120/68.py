import unittest
def maximum(arr, k):
    # Sort the list in ascending order
    arr.sort()
    return arr[:k]