Here's a Python script that solves the given problem with an efficient approach using `itertools.accumulate` and `collections.counter` to achieve the goal in O(n):
```python
from collections import Counter
from itertools import accumulate

def pluck(arr):
    even_values = [i for i in accumulate(arr) if i % 2 == 0]
    if not even_values:
        return []
    _, indices = Counter(even_values).most_common(1)
    return [indices[0], even_values.index(indices[0])]
```
This approach utilizes the `accumulate` function to iteratively filter even values from the input array. Subsequently, the `Counter` class is employed to ascertain and retrieve the index(es) of the smallest even value(s) present, along with their corresponding indices. The index of the plucked node is determined by indexing the `even_values` list with the smallest value.