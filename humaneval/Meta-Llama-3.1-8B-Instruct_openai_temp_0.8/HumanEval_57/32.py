```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of integers.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.

    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or all(l[i] >= l[i + 1] for i in range(len(l) - 1))


# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script uses the built-in `all()` function in Python, which returns `True` if all elements in an iterable are true. The generator expression inside `all()` checks each pair of adjacent elements in the list. If all pairs are either non-decreasing (`l[i] <= l[i + 1]`) or non-increasing (`l[i] >= l[i + 1]`), the function returns `True`; otherwise, it returns `False`.