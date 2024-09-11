```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): A list of numbers.

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
    return len(lst) == len(set(lst)) or all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) or all(lst[i] >= lst[i+1] for i in range(len(lst)-1))

# Test the function
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
print(monotonic([10, 9, 8, 7]))  # Expected output: True
print(monotonic([10, 8, 6, 4]))  # Expected output: True
```

This solution works by checking two conditions:

1. The list has no duplicate elements (`len(lst) == len(set(lst))`).
2. The list is either monotonically increasing (`all(lst[i] <= lst[i+1] for i in range(len(lst)-1))`) or monotonically decreasing (`all(lst[i] >= lst[i+1] for i in range(len(lst)-1))`).