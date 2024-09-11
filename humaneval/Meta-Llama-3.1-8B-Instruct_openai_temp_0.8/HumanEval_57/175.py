```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
    lst (list): A list of numbers.

    Returns:
    bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    """
    # Check if the list is empty
    if not lst:
        return True

    # Check if the list is monotonically increasing
    increasing = all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

    # Check if the list is monotonically decreasing
    decreasing = all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))

    # Return True if the list is monotonically increasing or decreasing
    return increasing or decreasing


# Test the function
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([]))  # True
print(monotonic([5]))  # True
print(monotonic([5, 5]))  # True
```

This script defines a function `monotonic` that takes a list of numbers as input and returns `True` if the list elements are monotonically increasing or decreasing, and `False` otherwise. It then tests the function with some examples.