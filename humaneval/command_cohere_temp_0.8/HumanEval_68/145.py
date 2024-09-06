Here's a Python script that solves the given problem with an efficient approach using `collections`:
```python
from collections import *

def pluck(arr):
    # Your code here!
    even, index = min(zip(arr, range(len(arr))), key=lambda x: x if x[0] % 2 == 0 else float('inf'))
    return [even[0], index] if even != float('-inf') else []
```
The approach uses `collections.min` with a custom `key` function to find the smallest even value in the array, considering the node's index as well. The code efficiently identifies the node with the desired properties.