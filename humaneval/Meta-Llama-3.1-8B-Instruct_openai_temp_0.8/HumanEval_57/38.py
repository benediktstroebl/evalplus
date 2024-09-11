```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): A list of numbers.

    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    # Check if list is empty
    if len(lst) < 2:
        return True  # A list of one or zero elements is considered monotonically increasing/decreasing

    # Compare each pair of adjacent elements
    increasing = decreasing = True
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            increasing = False
        if lst[i] > lst[i - 1]:
            decreasing = False

    # Return True if list elements are monotonically increasing or decreasing
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected: True
print(monotonic([1, 20, 4, 10]))  # Expected: False
print(monotonic([4, 1, 0, -10]))  # Expected: True
print(monotonic([1]))  # Expected: True
print(monotonic([]))  # Expected: True
```

This script defines a function `monotonic` that checks if the elements in a list are monotonically increasing or decreasing. It uses two flags, `increasing` and `decreasing`, to track whether the list elements are monotonically increasing or decreasing. If at any point a pair of adjacent elements does not satisfy the monotonic condition, the corresponding flag is set to `False`. Finally, the function returns `True` if and only if at least one of the flags is `True`.