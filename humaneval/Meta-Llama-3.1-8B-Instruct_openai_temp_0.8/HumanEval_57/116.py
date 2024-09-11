```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): The input list.

    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.

    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    is_increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    is_decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    return is_increasing or is_decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This script defines a function `monotonic` that checks if a list is monotonically increasing or decreasing. It uses the `all` function with a generator expression to check if all adjacent elements in the list satisfy the condition of being increasing or decreasing. The function returns `True` if the list is either increasing or decreasing and `False` otherwise. The test cases at the end demonstrate the function's usage.