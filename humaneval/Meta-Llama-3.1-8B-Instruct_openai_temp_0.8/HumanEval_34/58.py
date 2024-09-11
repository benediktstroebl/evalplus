```python
def unique(lst: list) -> list:
    """
    Return sorted unique elements in a list.

    Args:
        lst (list): The input list.

    Returns:
        list: A sorted list of unique elements.

    Examples:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script uses the built-in `set` function to remove duplicates and then the `sorted` function to sort the resulting list. The `unique` function takes a list as input and returns a new list with unique elements in sorted order. The example at the end demonstrates how to use this function.