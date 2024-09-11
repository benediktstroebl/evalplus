```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
    l (list): A list of elements.

    Returns:
    bool: True if the list elements are monotonically increasing or decreasing, False otherwise.

    Examples:
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    increasing = decreasing = True
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            increasing = False
        if l[i] > l[i-1]:
            decreasing = False
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected: True
print(monotonic([1, 20, 4, 10]))  # Expected: False
print(monotonic([4, 1, 0, -10]))  # Expected: True
```

This script defines a function `monotonic` that checks if the elements of a list are monotonically increasing or decreasing. It iterates over the list, keeping track of whether it's still increasing or decreasing. If it encounters a pair of elements that break this trend, it sets the corresponding flag to `False`. Finally, it returns `True` if the list is either strictly increasing or strictly decreasing, and `False` otherwise.