```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
        l (list): Input list

    Returns:
        list: Sorted list of unique elements

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, removes duplicates using the `set` data structure, and then sorts the unique elements in ascending order using the `sorted` function. The function is then tested with the provided example.