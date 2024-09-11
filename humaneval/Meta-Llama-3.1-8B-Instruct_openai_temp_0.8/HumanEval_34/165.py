```python
def unique(lst: list):
    """Return sorted unique elements in a list

    Args:
        lst (list): A list of elements.

    Returns:
        list: A sorted list of unique elements.

    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))

# Example usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list of elements as input, removes duplicates using the `set` function, and returns the sorted list of unique elements using the `sorted` function.