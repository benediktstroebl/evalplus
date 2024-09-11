```python
def unique(lst: list) -> list:
    """
    Returns sorted unique elements in a list.

    Args:
        lst (list): Input list containing elements.

    Returns:
        list: Sorted list of unique elements.

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, the `unique` function uses the built-in `set` data structure to remove duplicate elements from the input list, and then converts the set back into a list and sorts it.