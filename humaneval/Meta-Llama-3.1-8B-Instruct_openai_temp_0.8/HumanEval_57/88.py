```python
def monotonic(lst: list) -> bool:
    """Return True if list elements are monotonically increasing or decreasing."""
    
    # Check if list is empty
    if len(lst) < 2:
        return True
    
    # Check if list is monotonically increasing
    increasing = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    
    # Check if list is monotonically decreasing
    decreasing = all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
    
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
print(monotonic([]))  # Expected output: True
print(monotonic([1]))  # Expected output: True
```

This script defines a function `monotonic` that checks if the elements in a list are monotonically increasing or decreasing. It uses two helper functions with list comprehensions to check for these conditions. The function returns `True` if the list is monotonically increasing or decreasing, and `False` otherwise. The test cases at the end verify that the function behaves as expected.