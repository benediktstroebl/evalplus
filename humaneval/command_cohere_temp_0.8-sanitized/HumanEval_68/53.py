from collections import Counter
from itertools import accumulate
def pluck(arr):
    even_nodes = [i for i in accumulate(arr) if i % 2 == 0]
    if not even_nodes:
        return []

    # using Counter to get the minimum value and its index
    min_idx = Counter(even_nodes).most_common(1)[0][1]
    return [even_nodes[min_idx], min_idx]