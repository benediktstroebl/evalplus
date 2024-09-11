```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    Args:
        l (list): The input list to check.
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

# Test the function
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

In this script, I've added a docstring to the function `monotonic` to describe its behavior, parameters, and return value. I've also added a few test cases at the end to demonstrate how to use the function.