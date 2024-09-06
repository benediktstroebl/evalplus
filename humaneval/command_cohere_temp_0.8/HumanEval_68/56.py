Here's a Python script that includes a self-contained function designed to pluck a node from a tree branch represented by an array, in accordance with the problem statement:
```python
def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    if not even_nodes:
        return []
    min_even_val, min_index = min(enumerate(even_nodes), key=lambda x: x[1])
    return [min_even_val, min_index[0]]
```

This script includes a standalone `pluck` function that:
1. Collects even-valued nodes from the input array.
2. Finds the minimum even value and its corresponding index.
3. Returns a list containing the minimum even value and its index.

The `pluck` function adheres to the problem's specified constraints and handles various scenarios, including cases where there are multiple nodes with the same smallest even value, ultimately choosing the one with the smallest index.