```python
def monotonic(l: list):
    """
    Return True is list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of integers.

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

This script defines a function `monotonic` that checks whether the elements in a given list are monotonically increasing or decreasing. It iterates through the list from left to right, comparing each element with its predecessor. If it encounters a pair of elements where the second is smaller than the first, it sets `increasing` to `False`. If it encounters a pair where the second is larger than the first, it sets `decreasing` to `False`. Finally, it returns `True` if either `increasing` or `decreasing` is still `True`, indicating that the list is monotonically increasing or decreasing. Otherwise, it returns `False`.