from collections import Counter
from itertools import accumulate
def pluck(arr):
    if not arr:
        return []
    
    # Count occurrences of each value and determine smallest even value
    value_counts = Counter(arr)
    min_even_value = min((val for val, _ in value_counts.items() if val % 2 == 0), key=lambda x: (x, value_counts[x]))
    
    # Find the index of the smallest even value
    accum_results = list(accumulate(value_counts.get(min_even_value, []), operator.add))
    min_even_index = next(i for i, val in enumerate(accum_results) if val == 1) + 1

    return [min_even_value, min_even_index]