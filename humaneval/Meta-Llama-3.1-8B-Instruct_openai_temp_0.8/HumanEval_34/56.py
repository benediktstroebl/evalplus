```python
def unique(lst: list) -> list:
    """
    Return sorted unique elements in a list.

    Args:
    lst (list): The list from which to extract unique elements.

    Returns:
    list: A sorted list of unique elements.

    Example:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input and returns a sorted list of unique elements. The `set` function is used to remove duplicates, and `sorted` is used to sort the list in ascending order. The example at the end demonstrates how to use the function.