from itertools import accumulate, count
from collections import Counter
def pluck(arr):
    if not arr:
        return []

    # Find the smallest even value using accumulate
    even_vals = list(filter(lambda x: x % 2 == 0, arr))
    Accum = list(accumulate(even_vals))
    SmallestEvenVal = next((acc for acc in Accum if acc == min(Accum)), None)

    # Find the index of the smallest even value using counter
    Indices = list(count(1))
    CounterIndices = Counter(Indices)
    SmallestIndex = CounterIndices[SmallestEvenVal] if SmallestEvenVal in CounterIndices else None

    return [[SmallestEvenVal, SmallestIndex] if SmallestEvenVal and SmallestIndex else []]