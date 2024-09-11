```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of elements.

    Returns:
        bool: Whether the list elements are monotonically increasing or decreasing.

    Example:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    return all((l[i] <= l[i + 1] for i in range(len(l) - 1))) or all((l[i] >= l[i + 1] for i in range(len(l) - 1)))

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that checks if the elements of a list are monotonically increasing or decreasing. It uses the `all` function with a generator expression to check if all adjacent elements in the list satisfy the condition. The function returns `True` if the list is monotonically increasing or decreasing, and `False` otherwise. The script includes test cases to demonstrate the function's behavior.