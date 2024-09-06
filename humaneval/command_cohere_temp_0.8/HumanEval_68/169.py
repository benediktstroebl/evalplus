Here's a Python script that solves the given problem with an efficient approach using `itertools.accumulate` and `collections.Counter` to achieve the task:
```python
from collections import Counter
from itertools import accumulate

def pluck(arr):
    even_values = [i for i in accumulate( Counter(arr).values() ) if i % 2 == 0 ]
    if even_values:
        return [ min(even_values), even_values.index(min(even_values)) ]
    else:
        return []
```
The approach uses `Counter` to count the occurrences of each value and then filters out the even values using a generated `iterator`. The index of the plucked node is simply the index of the smallest even value in the accumulated results. The function returns the result as a list `[node_value, node_index]`.