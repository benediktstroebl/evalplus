```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    lst (list): The input list to check.
    
    Returns:
    bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    
    # Check if the list is empty or contains only one element
    if len(lst) < 2:
        return True
    
    # Check if the list is monotonically increasing
    increasing = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    
    # Check if the list is monotonically decreasing
    decreasing = all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
    
    # Return True if the list is either monotonically increasing or decreasing
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
print(monotonic([1, 2, 1]))  # Expected output: True
print(monotonic([]))  # Expected output: True
print(monotonic([5]))  # Expected output: True
```