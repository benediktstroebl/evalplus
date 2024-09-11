```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of integers.
    
    Returns:
    bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    """
    
    # Check if the list is empty
    if len(l) == 0:
        return True
    
    # Check if the list is monotonically increasing
    is_increasing = all(l[i] <= l[i + 1] for i in range(len(l) - 1))
    
    # Check if the list is monotonically decreasing
    is_decreasing = all(l[i] >= l[i + 1] for i in range(len(l) - 1))
    
    # Return True if the list is either monotonically increasing or decreasing
    return is_increasing or is_decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
print(monotonic([]))  # Expected output: True
print(monotonic([5]))  # Expected output: True
```

This script uses the `all()` function with a generator expression to check if the list elements are either monotonically increasing or decreasing. The `all()` function returns `True` if all elements of the iterable are true. If at least one element is false, it returns `False`. The script also includes test cases to verify its correctness.