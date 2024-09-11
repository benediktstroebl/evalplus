```python
def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.

    Args:
    l (list): A list of numbers.

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
        if l[i] < l[i - 1]:
            increasing = False
        if l[i] > l[i - 1]:
            decreasing = False

    return increasing or decreasing
```

This script defines a function `monotonic` that takes a list of numbers as input and returns `True` if the list elements are monotonically increasing or decreasing and `False` otherwise. The function uses two flags `increasing` and `decreasing` to track whether the list is monotonically increasing or decreasing respectively. It iterates over the list from the second element to the end, checking if the current element is greater or less than the previous one. If a pair of elements has the wrong order, the corresponding flag is set to `False`. The function returns `True` if either flag is still `True` after the iteration, indicating that the list is monotonically increasing or decreasing.