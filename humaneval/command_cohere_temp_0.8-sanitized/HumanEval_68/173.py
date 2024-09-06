from itertools import accumulate, chain
from collections import Counter
def pluck(arr):
    even_values = list(chain.from_iterable(accumulate((x % 2 == 0 for x in arr), max)))
    indices = Counter(zip(even_values, arr)).most_common()[0][1][0] if even_values else []
    return [indices, min(indices)] if indices else []