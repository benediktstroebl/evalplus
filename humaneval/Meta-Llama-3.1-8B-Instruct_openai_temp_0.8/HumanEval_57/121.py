```python
def monotonic(lst: list):
    """Return True is list elements are monotonically increasing or decreasing.

    Args:
        lst (list): A list of numbers.

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

    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            decreasing = False
        elif lst[i] < lst[i - 1]:
            increasing = False

    return increasing or decreasing
```

This script defines a function `monotonic` that checks if the elements of a list are monotonically increasing or decreasing. It uses two flags, `increasing` and `decreasing`, to track whether the list elements are increasing or decreasing respectively. If at any point the list elements are not increasing or decreasing, the corresponding flag is set to `False`. Finally, the function returns `True` if either flag is still `True`, indicating that the list elements are monotonically increasing or decreasing, and `False` otherwise.