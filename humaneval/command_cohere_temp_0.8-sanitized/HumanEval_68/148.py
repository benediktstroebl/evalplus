from typing import List
from itertools import accumulate
from collections import Counter
def pluck(arr: List[int]) -> List[int]:
    even_nodes = [i for i, num in enumerate(arr) if num % 2 == 0]
    if not even_nodes:
        return []

    # Using Counter to get the minimum even value and its index
    min_value, min_index = Counter(even_nodes).most_common(1)[0]
    
    return [min_value, min_index]