```python
def unique(l: list):
    """
    Return sorted unique elements in a list.

    Args:
        l (list): A list of elements.

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

This Python script defines a function `unique` that takes a list `l` as input and returns a sorted list of unique elements. It uses the `set` function to remove duplicates and the `sorted` function to sort the list. The example usage at the end demonstrates how to use the function.