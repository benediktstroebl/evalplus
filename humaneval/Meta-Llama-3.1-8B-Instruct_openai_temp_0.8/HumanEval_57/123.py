```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of elements to check.

    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    # Check if list is empty
    if len(l) < 2:
        return True

    increasing = decreasing = True

    # Check for increasing sequence
    for i in range(len(l) - 1):
        if l[i] >= l[i + 1]:
            increasing = False
        # Check for decreasing sequence
        if l[i] <= l[i + 1]:
            decreasing = False

    return increasing or decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected: True
print(monotonic([1, 20, 4, 10]))  # Expected: False
print(monotonic([4, 1, 0, -10]))  # Expected: True
print(monotonic([]))  # Expected: True
print(monotonic([5]))  # Expected: True
```

This script includes a function `monotonic` that checks if a list's elements are monotonically increasing or decreasing. It iterates over the list to compare each element with its neighbors and sets `increasing` and `decreasing` flags. The function returns `True` if either `increasing` or `decreasing` is `True`, meaning the list's elements are monotonically increasing or decreasing. It handles edge cases, including empty lists and lists with a single element.