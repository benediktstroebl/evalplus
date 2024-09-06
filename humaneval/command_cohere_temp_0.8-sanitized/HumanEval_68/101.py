from collections import Counter
from itertools import accumulate
def pluck(arr):
    if not arr:
        return []
    
    # Count occurrences of each value and index
    value_count = Counter(zip(arr, range(len(arr))))
    
    # Filter for even values and get minimum