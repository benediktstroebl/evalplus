```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
        l (list): The input list.

    Returns:
        list: A sorted list of unique elements.

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

However, the function does not handle the order of elements in the original list. If you want to preserve the order, you can use the following version:

```python
def unique_ordered(l: list):
    """Return sorted unique elements in a list while preserving order

    Args:
        l (list): The input list.

    Returns:
        list: A list of unique elements in the original order.

    Example:
        >>> unique_ordered([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [5, 3, 2, 9, 0, 123]
    """
    seen = set()
    return [x for x in l if not (x in seen or seen.add(x))]

# Test the function
print(unique_ordered([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```