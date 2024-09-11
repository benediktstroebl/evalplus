```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): The input list to check for monotonicity.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    # Check if the list is empty
    if len(lst) == 0:
        return True  # An empty list is considered monotonic

    # Check if the list is monotonically increasing
    is_increasing = all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

    # Check if the list is monotonically decreasing
    is_decreasing = all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))

    # Return True if the list is either monotonically increasing or decreasing
    return is_increasing or is_decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
print(monotonic([]))  # Expected output: True
print(monotonic([5]))  # Expected output: True
```