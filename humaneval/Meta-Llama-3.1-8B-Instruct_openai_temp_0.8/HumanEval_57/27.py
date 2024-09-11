```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
    A list is monotonically increasing if each element is greater than or equal to the previous one.
    A list is monotonically decreasing if each element is less than or equal to the previous one.
    
    Args:
        l (list): The input list.
    
    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    
    # Check if the list is monotonically increasing
    increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    
    # Check if the list is monotonically decreasing
    decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    
    # Return True if the list is either monotonically increasing or decreasing
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This script defines a function `monotonic` that checks if a list is monotonically increasing or decreasing. It uses the `all` function to check if all elements in the list satisfy the condition. The function returns `True` if the list is either monotonically increasing or decreasing, and `False` otherwise. The script includes test cases to demonstrate the function's usage.