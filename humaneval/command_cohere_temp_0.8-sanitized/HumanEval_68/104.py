from typing import List
from itertools import accumulate, count
from collections import Counter
def pluck(arr: List[int]) -> List[int]:
    even_nodes = [i for i in accumulate(Counter(arr).items()) if i[1] % 2 == 0]
    if even_nodes:
        return min(even_nodes, key=lambda x: x[1])[0:] + [min(even_nodes, key=lambda x: x[1])[1]]
    return []