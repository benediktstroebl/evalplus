Here's a Python script that solves the given problem with an efficient approach using `itertools.accumulate` and `collections.Counter`:
```python
from typing import List
from itertools import accumulate, count
from collections import Counter

def pluck(arr: List[int]) -> List[int]:
    even_nodes = [i for i in accumulate(Counter(arr).items()) if i[1] % 2 == 0]
    if even_nodes:
        return min(even_nodes, key=lambda x: x[1])[0:] + [min(even_nodes, key=lambda x: x[1])[1]]
    return []
```
This approach uses the `itertools.accumulate` function to create a list of tuples where each tuple contains the current value of the input list and its index. Then, we filter these tuples to include only even values and use `collections.Counter` to automatically assign indices to elements with the same value. The result is a list of tuples, where each tuple contains the value of the node and its index. From these, we choose the node with the smallest index, in case of a tie. 

The function returns `[]` if the input array is empty or has no even-valued nodes. You can use this function to pluck a node from the array according to the problem statement.