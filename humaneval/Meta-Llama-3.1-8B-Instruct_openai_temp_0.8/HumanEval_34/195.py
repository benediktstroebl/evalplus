```python
def unique(l: list) -> list:
    """Return sorted unique elements in a list

    Args:
    l (list): A list of elements

    Returns:
    list: A sorted list of unique elements

    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates, then convert back to list
    unique_list = list(set(l))
    # Sort the list in ascending order
    unique_list.sort()
    return unique_list

# Example usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` which takes a list as input, removes duplicates by converting it to a set (which automatically removes duplicates), and then converts it back to a list. It then sorts the list in ascending order using the `sort` method. The function is documented with a docstring, and includes a doctest to verify its behavior.