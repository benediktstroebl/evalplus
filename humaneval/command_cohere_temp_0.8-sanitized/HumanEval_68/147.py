from collections import Counter
from itertools import accumulate
def pluck(arr):
    even_values = [val for val in accumulate(arr) if val % 2 == 0]
    if not even_values:
        return []
    min_value, min_index = min(Counter(even_values).items()), even_values.index(min(even_values))
    return [min_value, min_index]