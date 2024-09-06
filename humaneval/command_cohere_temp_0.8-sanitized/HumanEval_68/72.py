from collections import Counter
from itertools import accumulate
def pluck(arr):
    even_nodes = [val for val in accumulate(arr) if val % 2 == 0]
    if even_nodes:
        min_value, min_index = min(Counter(even_nodes).items()), even_nodes.index(min(even_nodes))
        return [min_value, min_index]
    else:
        return []