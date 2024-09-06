from collections import Counter
from itertools import accumulate
def pluck(arr):
    even_values = [i for i in accumulate( Counter(arr).values() ) if i % 2 == 0 ]
    if even_values:
        return [ min(even_values), even_values.index(min(even_values)) ]
    else:
        return []