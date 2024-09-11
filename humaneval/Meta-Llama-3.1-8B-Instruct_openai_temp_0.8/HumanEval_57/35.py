```python
def monotonic(lst: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
    lst (list): A list of numbers.

    Returns:
    bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) or \
           all(lst[i] >= lst[i+1] for i in range(len(lst)-1))


# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
print(monotonic([1, 2, 3, 4]))  # Expected output: True
print(monotonic([4, 3, 2, 1]))  # Expected output: True
print(monotonic([1, 2, 5, 4]))  # Expected output: False
```

This Python function uses list comprehension and the `all()` function to check if all adjacent pairs of elements in the list satisfy the monotonic property (either increasing or decreasing). If both increasing and decreasing are True, it will return True. If neither is True, it will return False.