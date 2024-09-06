from itertools import accumulate, count
from collections import Counter
def pluck(arr):
    even_nodes = [i for i in accumulate(arr) if i % 2 == 0]
    if not even_nodes:
        return []
    _, min_index = Counter(even_nodes).most_common(1)[0]
    return [min_index, min_index]