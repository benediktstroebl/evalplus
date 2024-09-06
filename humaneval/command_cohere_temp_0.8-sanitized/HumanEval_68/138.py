from typing import List
from itertools import accumulate, chain
from collections import Counter
def pluck(arr: List[int]) -> List[int]:
    even_values = list(filter(lambda x: x % 2 == 0, arr))
    num_occurrences = Counter(chain(even_values, [0]))
    
    results = []
    for idx, occur in enumerate(accumulate(num_occurrences.values())):
        if occur == 0:
            results.append([num_occurrences[0], -1])
        if occur == 1:
            results.append([num_occurrences[1], idx])

    return results if results else [[]]