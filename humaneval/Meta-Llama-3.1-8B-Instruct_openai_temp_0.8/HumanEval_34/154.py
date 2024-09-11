```python
def unique(l: list):
    """
    Return sorted unique elements in a list

    Args:
        l (list): A list of elements

    Returns:
        list: A sorted list of unique elements

    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script uses the built-in Python `set` function to remove duplicates and the `sorted` function to sort the resulting list. The `set` function automatically removes duplicate elements, and then the `sorted` function sorts the remaining elements in ascending order.