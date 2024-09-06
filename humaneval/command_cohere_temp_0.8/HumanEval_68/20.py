Here's a Python script that solves the given problem with an efficient approach using the `itertools.accumulate` function to find the smallest even value and its index:
```python
from itertools import accumulate

def pluck(arr):
    even_values = [x for x in accumulate(arr) if x % 2 == 0]
    if even_values:
        return [min(even_values), even_values.index(min(even_values))]
    return []
```

The `pluck` function takes an input list arr and finds the smallest even value in the list using the `itertools.accumulate` function and a list comprehension. After finding the even values, it determines the index of the plucked node from the accumulated even values list using the `index` method. The function returns a list containing the smallest even value and its index, or an empty list if no even values are found.

This approach efficiently accumulates even values and their indices in a single pass, making it effective for large input arrays.