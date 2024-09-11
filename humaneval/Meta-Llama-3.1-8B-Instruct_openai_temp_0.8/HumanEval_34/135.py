```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
        l (list): The input list

    Returns:
        list: A sorted list of unique elements

    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))


# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list `l` as input. It uses the built-in `set` function to remove duplicates from the list and then sorts the resulting set using the `sorted` function. The result is a sorted list of unique elements.