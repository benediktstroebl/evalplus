```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of numbers.

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
    is_increasing = all(x <= y for x, y in zip(l, l[1:]))
    is_decreasing = all(x >= y for x, y in zip(l, l[1:]))
    return is_increasing or is_decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([1, 2, 3, 4, 5]))  # True
print(monotonic([5, 4, 3, 2, 1]))  # True
print(monotonic([1, 1, 1, 1, 1]))  # True
```