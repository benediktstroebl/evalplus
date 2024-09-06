from typing import List
from itertools import accumulate
from collections import Counter
def pluck(arr: List[int]) -> List[int]:
    even_values = [x for x in accumulate(arr) if x % 2 == 0]
    if even_values:
        min_value, min_index = min(Counter(even_values).items()), even_values.index(min(even_values))
        return [min_value, min_index]
    else:
        return []