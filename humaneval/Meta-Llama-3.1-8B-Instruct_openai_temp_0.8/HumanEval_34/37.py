```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
        l (list): A list of integers.

    Returns:
        list: A sorted list of unique integers.

    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
print(unique([1, 1, 1, 2, 2, 3, 4, 4, 5]))
print(unique([]))  # An empty list
```

In this script, we use Python's built-in `set` data structure, which automatically removes duplicates. We then convert this set back to a list and sort it using the `sorted` function. This approach is efficient because it has a time complexity of O(n), where n is the number of elements in the list.