### Unique Elements in a List
#### Python Script to Return Sorted Unique Elements

```python
def unique(l: list):
    """
    Return sorted unique elements in a list.

    Args:
    l (list): The input list.

    Returns:
    list: A list of unique elements in sorted order.

    Example:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [0, 2, 3, 5, 9, 123]
```

This script uses the built-in `set` function to remove duplicates from the list and the `sorted` function to sort the resulting list in ascending order.