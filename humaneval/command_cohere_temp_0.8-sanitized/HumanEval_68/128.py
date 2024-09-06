from typing import List
from itertools import accumulate, chain
from collections import Counter
def pluck(nodes: List[int]) -> List[str]:
    even_nodes = [x for x in accumulate(nodes) if x % 2 == 0]
    return [_pluck_smallest(cnt) for cnt in Counter(even_nodes).items()] if even_nodes else [""]
def _pluck_smallest(cnt: Counter[int]) -> List[int]:
    return [min(cnt), min(cnt.keys())]