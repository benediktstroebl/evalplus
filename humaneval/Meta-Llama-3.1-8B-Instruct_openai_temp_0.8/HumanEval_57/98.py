```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of numbers.
    
    Returns:
    bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    
    # Check if the list is empty
    if len(l) < 2:
        return True
    
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

This script works by first checking if the list has at least two elements. If it doesn't, the list is considered to be monotonically increasing or decreasing by default. Then, it checks if the list is monotonically increasing by comparing each element with its next one. It does the same for the decreasing case. If the list is either monotonically increasing or decreasing, the function returns True. Otherwise, it returns False.