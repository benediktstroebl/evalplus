from typing import List
from itertools import accumulate
from collections import Counter
def pluck(arr: List[int]) -> List[int]:
    even_nodes = [n for n in arr if n % 2 == 0]
    if not even_nodes:
        return []

    # Find the index of the smallest even node
    smallest_index = min(Counter(even_nodes).items(), key=lambda x: x[1])[0]

    # Use accumulate to find the smallest even node's value
    accum_iter = accumulate(even_nodes)
    value_at_smallest_index = next(x for x in accum_iter if x[0] == smallest_index)

    return [value_at_smallest_index[1], smallest_index]
arr = [4, 2, 3]