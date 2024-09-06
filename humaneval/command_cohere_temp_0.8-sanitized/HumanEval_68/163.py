from collections import Counter
from itertools import accumulate
def pluck(arr):
    even_values = [i for i in accumulate(arr) if i % 2 == 0]
    if not even_values:
        return []
    _, indices = Counter(even_values).most_common(1)
    return [indices[0], even_values.index(indices[0])]