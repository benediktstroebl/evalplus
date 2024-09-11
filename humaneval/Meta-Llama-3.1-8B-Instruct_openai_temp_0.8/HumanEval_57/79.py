```python
def monotonic(lst: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
    lst (list): A list of numbers.

    Returns:
    bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) or all(lst[i] >= lst[i+1] for i in range(len(lst)-1))

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that checks if the elements in a list are monotonically increasing or decreasing. It uses the `all` function with a generator expression to check if all elements in the list are either non-decreasing or non-increasing. The `range(len(lst)-1)` is used to avoid an `IndexError` when checking the last element in the list. The test cases demonstrate the function's behavior with different input lists.