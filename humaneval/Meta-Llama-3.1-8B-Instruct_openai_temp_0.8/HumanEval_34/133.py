```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list `l` as input, converts it to a set to remove duplicates, and then sorts the resulting set in ascending order. The `sorted` function is used with the `set` constructor to achieve this. The example usage demonstrates how to call the `unique` function with a sample list.