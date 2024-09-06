from typing import List
from itertools import accumulate, count
from collections import Counter
def pluck(arr: List[int]) -> List[int]:
    even_nodes = [i for i in accumulate(arr) if i % 2 == 0]
    if not even_nodes:
        return []

    # using Counter to find the minimum even value and its index
    counter = Counter(even_nodes)
    min_value, min_index = counter.elements()[0]
    return [min_value, min_index]