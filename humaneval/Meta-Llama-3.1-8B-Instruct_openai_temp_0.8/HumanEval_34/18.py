```python
def unique(lst: list) -> list:
    """Return sorted unique elements in a list

    Args:
        lst (list): The input list.

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

This script defines a function `unique` that takes a list as input, removes duplicates using a set, and then sorts the resulting list. The `sorted` function is used to sort the list in ascending order by default. The `set` data structure is used to remove duplicate elements from the list. The function includes a docstring that describes its purpose, arguments, return value, and includes an example use case.