```python
def unique(l: list):
    """
    Return sorted unique elements in a list.

    Args:
        l (list): Input list of elements.

    Returns:
        list: Sorted list of unique elements.

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, the `unique` function uses the built-in `set` function to remove duplicates from the input list, and then sorts the resulting set using the `sorted` function. The result is a sorted list of unique elements.