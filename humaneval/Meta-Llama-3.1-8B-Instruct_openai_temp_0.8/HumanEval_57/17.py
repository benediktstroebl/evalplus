```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): The input list to check.

    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.

    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """

    # Check if list is empty
    if len(l) == 0:
        return False

    # Check if list is increasing
    increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))

    # Check if list is decreasing
    decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))

    # Return True if list is either increasing or decreasing
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected: True
print(monotonic([1, 20, 4, 10]))  # Expected: False
print(monotonic([4, 1, 0, -10]))  # Expected: True
print(monotonic([1, 1, 1, 1]))  # Expected: True
print(monotonic([]))  # Expected: False
```

This script defines a function `monotonic` that takes a list `l` as input and returns `True` if the list elements are monotonically increasing or decreasing. It first checks if the list is empty, and if so, returns `False` because an empty list cannot be considered monotonic. Then it checks if the list is increasing or decreasing by using the `all` function to check if all pairs of consecutive elements satisfy the respective condition. If both conditions are met, the function returns `True`, otherwise it returns `False`. The test cases are included to demonstrate the function's usage and expected behavior.