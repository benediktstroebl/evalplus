from collections import Counter
from itertools import accumulate
def pluck(arr):
    even_values = Counter(x for x in accumulate(arr) if x % 2 == 0)
    smallest_idx = min(even_values.values(), key=lambda x: x[1])[1]
    return smallest_idx and [smallest_idx, smallest_idx] or []