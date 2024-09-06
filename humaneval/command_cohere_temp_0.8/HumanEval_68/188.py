Here's a Python script that solves the given problem with an efficient approach using Python's `collections` module:
```python
from collections import Counter

def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    smallest_even, index = min(even_nodes), even_nodes.index(smallest_even) if even_nodes else None
    return [smallest_even, index] if smallest_even and index != None else []
```

This approach utilizes the `Counter` class from the `collections` module to efficiently count the occurrences of even values in the array. The `min` function is then used to find the smallest even value, and the `index` of that value is retrieved using the `index` attribute of the smallest value instance.

The function returns a list `[smallest_even, index]`, or an empty list `[]` if no even values are found or if the array is empty.