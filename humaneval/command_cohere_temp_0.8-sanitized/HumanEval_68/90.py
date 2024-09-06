from collections import Counter
from itertools import accumulate
def pluck(arr):
    even_values = [i for i in accumulate( Counter(arr).values() ) if i % 2 == 0 ]
    smallest_even, idx = (min(even_values), even_values.index(min(even_values))) if even_values else None
    return [smallest_even, idx] if smallest_even is not None else []