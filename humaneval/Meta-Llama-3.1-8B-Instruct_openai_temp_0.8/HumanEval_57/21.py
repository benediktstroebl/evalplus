```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l: A list of numbers.
    
    Returns:
    bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True
    
    for i in range(1, len(l)):
        # List is not increasing if an element is greater than the previous one
        increasing &= l[i] >= l[i - 1]
        
        # List is not decreasing if an element is smaller than the previous one
        decreasing &= l[i] <= l[i - 1]
    
    # List is monotonic if it is either increasing or decreasing
    return increasing or decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected: True
print(monotonic([1, 20, 4, 10]))  # Expected: False
print(monotonic([4, 1, 0, -10]))  # Expected: True
```