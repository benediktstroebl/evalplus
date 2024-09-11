```python
def unique(lst: list) -> list:
    """
    Return sorted unique elements in a list.

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

In this script, we use the built-in `set()` function to remove duplicates from the list and then pass it to the `sorted()` function to sort the elements in ascending order. The result is a list of unique elements in sorted order.