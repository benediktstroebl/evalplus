from itertools import accumulate, chain
from collections import Counter
def pluck(arr):
    if not arr:
        return []

    # Find the smallest even value using accumulate, starting from odd
    odd, even = divmod(next(accumulate(arr), 0), 2)
    even_idx = next(i for i, v in enumerate(accumulate(arr), odd) if v == even)

    # Use counter to get the index of the smallest even value
    # Counter remembers the index of the smallest occurrence of each value
    _, idx = Counter(chain([even], arr)).most_common(1)[0]

    return [even, even_idx or idx]