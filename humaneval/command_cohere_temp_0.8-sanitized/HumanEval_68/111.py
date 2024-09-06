from collections import Counter
from itertools import accumulate
def pluck(arr):
    if not arr:
        return []

    # Count occurrences of each value and index
    value_count = Counter(zip(arr, range(len(arr))))
    
    # Find the smallest even value using the 'most_common' method
    smallest_even_value = min(value_count.most_common(), key=lambda x: x[1])[0]
    
    # Find the index of the smallest even value using the 'elements' method
    smallest_even_index = value_count[smallest_even_value]
    
    return [smallest_even_value, smallest_even_index]