```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of numbers.

    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True

    for i in range(1, len(l)):
        if l[i] < l[i - 1]:  # If the current element is smaller than the previous one, the list is not increasing.
            increasing = False
        if l[i] > l[i - 1]:  # If the current element is larger than the previous one, the list is not decreasing.
            decreasing = False

    return increasing or decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This script defines a function `monotonic` that takes a list `l` as input and returns `True` if the list elements are monotonically increasing or decreasing, and `False` otherwise. It then tests the function with the provided test cases.