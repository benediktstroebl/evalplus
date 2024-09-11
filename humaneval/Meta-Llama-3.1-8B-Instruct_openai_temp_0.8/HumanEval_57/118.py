```python
def monotonic(l: list):
    """
    Return True is list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of numbers.

    Returns:
        bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True

    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            increasing = False
        if l[i] > l[i - 1]:
            decreasing = False

    return increasing or decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that checks if the elements of a list are monotonically increasing or decreasing. It iterates over the list, comparing each element with its predecessor. If it finds a pair of elements where the second is smaller than the first (in case of increasing list) or larger than the first (in case of decreasing list), it sets `increasing` or `decreasing` to `False` respectively. After iterating over the entire list, it returns `True` if either `increasing` or `decreasing` is `True`, indicating that the list is monotonically increasing or decreasing.