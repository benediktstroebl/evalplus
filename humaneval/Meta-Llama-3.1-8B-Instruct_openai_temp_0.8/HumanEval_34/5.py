```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, removes duplicates by converting it to a set, and returns the elements in sorted order. The test at the end demonstrates the function's behavior. 

The function works as follows:

1. `set(l)` removes duplicates from the list by treating it as a set, which automatically removes any duplicate elements.
2. `sorted(...)` sorts the resulting set in ascending order.
3. The sorted set is returned as the result.

Note that this function is case-sensitive and considers integers and strings as different elements. If you need to ignore case or other differences (e.g., consider "3" and "03" as the same element), you may need to modify the function accordingly.