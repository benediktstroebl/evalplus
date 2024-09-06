from collections import Counter
from itertools import accumulate
def pluck(arr):
    even_values = [val for val in accumulate(arr) if val % 2 == 0]
    if not even_values:
        return []
    _, min_idx = Counter(even_values).most_common(1)[0]
    return [min_idx, min_idx]