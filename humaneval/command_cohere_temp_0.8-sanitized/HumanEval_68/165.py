import random
import unittest
from collections import Counter
def pluck(arr):
    if not arr:
        return []
    return min((Counter(arr[i:])).items() for i in range(len(arr)) if arr[i] % 2 == 0)