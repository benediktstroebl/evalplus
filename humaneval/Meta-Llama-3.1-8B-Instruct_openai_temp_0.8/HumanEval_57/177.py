```python
def monotonic(lst):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        lst (list): A list of elements.
    
    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    is_increasing = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    is_decreasing = all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
    
    return is_increasing or is_decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([1, 2, 3, 4, 5]))  # True
print(monotonic([5, 4, 3, 2, 1]))  # True
print(monotonic([1, 3, 2, 4, 5]))  # False
```

This script uses the `all()` function to check if all elements in the list are monotonically increasing or decreasing. If all elements meet either of these criteria, the function returns `True`, otherwise it returns `False`. The test cases provided demonstrate the function's behavior on various input scenarios.