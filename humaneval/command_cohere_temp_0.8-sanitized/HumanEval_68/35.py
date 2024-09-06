import numpy as np
from collections import *
def pluck(arr):
    # your task is to pluck one of the nodes and return it
    if not arr or max(arr) % 2 != 0:
        return []

    # Find the smallest even value and its index using min and key
    # Then use numpy's searchsorted to find the index of the second occurrence (if any)