```python
def unique(input_list: list) -> list:
    """
    Return sorted unique elements in a list.

    Args:
    input_list (list): A list of elements

    Returns:
    list: A sorted list of unique elements

    Example:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(input_list))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, converts it to a set to remove duplicates, and then converts it back to a list and sorts it. The `set` data structure in Python is an unordered collection of unique elements. By converting the list to a set and then back to a list, we remove duplicates. The `sorted` function is then used to sort the list in ascending order.