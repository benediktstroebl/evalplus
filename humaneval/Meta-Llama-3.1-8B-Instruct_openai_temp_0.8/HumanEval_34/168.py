```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
        l (list): The input list.

    Returns:
        list: A sorted list of unique elements.

    Examples:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script uses Python's built-in `set` data structure to remove duplicates from the list, and the `sorted` function to sort the resulting list in ascending order. The `set` data structure automatically removes any duplicate elements, and the `sorted` function sorts the elements in ascending order.