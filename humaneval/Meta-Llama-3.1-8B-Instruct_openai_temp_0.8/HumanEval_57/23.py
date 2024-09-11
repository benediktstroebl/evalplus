```python
def monotonic(lst: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        lst (list): A list of elements to check.
    
    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    # Check if list is monotonically increasing
    increasing = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    
    # Check if list is monotonically decreasing
    decreasing = all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
    
    # Return True if list is either monotonically increasing or decreasing
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
print(monotonic([2, 4, 6, 8, 10]))  # Expected output: True
print(monotonic([10, 9, 8, 7, 6]))  # Expected output: True
```

This script defines a function `monotonic` that takes a list of elements as input and returns `True` if the list elements are monotonically increasing or decreasing, and `False` otherwise. The function uses list comprehensions to check if the list elements are either monotonically increasing or decreasing. The test cases are included at the end of the script to demonstrate the function's usage.