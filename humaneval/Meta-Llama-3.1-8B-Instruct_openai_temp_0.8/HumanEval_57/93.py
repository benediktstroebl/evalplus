```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
    l (list): A list of numbers.

    Returns:
    bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    if len(l) < 2:
        return True

    increasing = decreasing = True

    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            increasing = False
        if l[i] > l[i-1]:
            decreasing = False

    return increasing or decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([5]))  # True
print(monotonic([5, 5]))  # True
```

This script defines a function `monotonic` that checks whether a given list is monotonically increasing or decreasing. It iterates over the list and checks if each element is greater than (decreasing) or less than (increasing) the previous one. If it finds any pair of elements that don't follow the rule, it sets the corresponding flag to `False`. Finally, it returns `True` if either flag is still `True`, meaning the list is either increasing or decreasing.