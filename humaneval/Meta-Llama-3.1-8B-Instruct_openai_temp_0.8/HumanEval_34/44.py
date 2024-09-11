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

# Example usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list `l` as input, converts it into a set (which automatically removes duplicates), and then sorts the resulting set. The result is a sorted list of unique elements. The example usage at the end demonstrates how to use this function.