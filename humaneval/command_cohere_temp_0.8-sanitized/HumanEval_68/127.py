from collections import Counter
from itertools import accumulate
def pluck(arr):
    even_sum = sum(x for x in arr if x % 2 == 0)
    indices = Counter(accumulate(arr))
    smallest_index, _ = indices.most_common(1)[0]
    return [even_sum, smallest_index] if even_sum != 0 else []