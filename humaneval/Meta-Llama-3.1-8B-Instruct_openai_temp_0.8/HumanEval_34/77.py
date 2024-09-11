```python
def unique(l: list):
    """Return sorted unique elements in a list

    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]

    Args:
        l (list): A list of elements

    Returns:
        list: A sorted list of unique elements from the input list
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list `l` as input and returns a sorted list of unique elements from `l`. It uses the `set` data structure to remove duplicates, which returns a set of unique elements. The `sorted` function is then used to sort the set in ascending order, and the result is returned as a list. The script also includes a test case to demonstrate the function's usage.