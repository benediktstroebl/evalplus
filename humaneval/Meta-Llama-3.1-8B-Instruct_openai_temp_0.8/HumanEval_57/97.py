```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of elements.

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
    increasing = decreasing = True

    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            decreasing = False
        if l[i] > l[i + 1]:
            increasing = False

    return increasing or decreasing


# Test the function
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This script defines a function `monotonic` that takes a list of elements as input and returns `True` if the elements are monotonically increasing or decreasing, and `False` otherwise. It uses two flags, `increasing` and `decreasing`, to track whether the elements are increasing or decreasing, respectively. It then iterates over the list, updating these flags as necessary. Finally, it returns `True` if either flag is `True`, indicating that the elements are monotonically increasing or decreasing.