```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
        l (list): A list of elements.

    Returns:
        list: A sorted list of unique elements.

    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [0, 2, 3, 5, 9, 123]
```

In this script, we're using Python's built-in `set` function to remove duplicates, and the `sorted` function to sort the unique elements in ascending order. This approach has a time complexity of O(n log n), where n is the number of elements in the list.