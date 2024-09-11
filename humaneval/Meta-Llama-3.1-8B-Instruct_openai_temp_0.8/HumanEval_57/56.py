### Monotonic List Checker

```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): List of numbers

    Returns:
        bool: True if list is monotonically increasing or decreasing, False otherwise
    """
    increasing = decreasing = True

    for i in range(1, len(lst)):
        # If current element is less than previous, list is not increasing
        if lst[i] < lst[i - 1]:
            increasing = False
        # If current element is greater than previous, list is not decreasing
        if lst[i] > lst[i - 1]:
            decreasing = False

    return increasing or decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This script defines a function `monotonic` that takes a list of numbers as input and returns `True` if the list is monotonically increasing or decreasing, and `False` otherwise. The function uses two flags `increasing` and `decreasing` to track whether the list is increasing or decreasing. It then iterates over the list, updating these flags based on the comparison between adjacent elements. The function returns `True` if either of the flags is still `True` after the iteration.