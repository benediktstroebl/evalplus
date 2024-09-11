```python
def unique(l: list) -> list:
    """Return sorted unique elements in a list

    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Using a set to remove duplicates, then converting back to a list and sorting
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, removes duplicates by converting it to a set, and then sorts the resulting set before returning it. The function is then tested with an example output.