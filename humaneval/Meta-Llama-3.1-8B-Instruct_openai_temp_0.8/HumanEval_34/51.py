```python
def unique(lst: list) -> list:
    """Return sorted unique elements in a list

    Args:
        lst (list): The input list

    Returns:
        list: A sorted list of unique elements

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script:

1. The `set(lst)` function removes duplicate elements from the list.
2. The `sorted()` function sorts the unique elements in ascending order.
3. The `unique()` function is then called with the test list and its result is printed.