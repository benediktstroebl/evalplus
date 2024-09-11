```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True

    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            decreasing = False
        elif lst[i] > lst[i + 1]:
            increasing = False

    return increasing or decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected: True
print(monotonic([1, 20, 4, 10]))  # Expected: False
print(monotonic([4, 1, 0, -10]))  # Expected: True
```

This script defines a function `monotonic` that checks whether the elements in the input list are monotonically increasing or decreasing. It uses a flag to track whether the list is increasing or decreasing, and returns `True` if the list meets either condition. The test cases at the end verify the function's correctness.