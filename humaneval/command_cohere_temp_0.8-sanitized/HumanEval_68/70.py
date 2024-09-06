from collections import Counter
from itertools import accumulate
def pluck(arr):
    if not arr:
        return []

    # Count occurrences of each value and index them with their index
    cnt = Counter(zip(arr, list(range(len(arr)))))
    
    # Filter for even values and get the minimum value