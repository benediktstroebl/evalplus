```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

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

    # Check if the list is empty or has one element
    if len(l) < 2:
        return True

    # Check if the list is increasing or decreasing
    increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))

    # Return True if the list is either increasing or decreasing
    return increasing or decreasing

# Test the function
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
print(monotonic([5]))  # Expected output: True
print(monotonic([]))  # Expected output: True
```

This script defines a function `monotonic` that checks if the elements of a list are monotonically increasing or decreasing. It uses the `all` function in combination with a generator expression to check if the list is increasing or decreasing. If the list has one or zero elements, it is considered monotonic, so the function returns `True` in these cases.