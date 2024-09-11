```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
        l (list): The input list of elements.

    Returns:
        list: A sorted list of unique elements from the input list.

    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))  # Convert list to set (removing duplicates) and then sort it

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [0, 2, 3, 5, 9, 123]
```

This script defines a function `unique()` that takes a list as input, removes duplicates by converting it to a set, and then sorts the set in ascending order before returning it as a list. The example usage demonstrates the function's behavior with the provided test case.