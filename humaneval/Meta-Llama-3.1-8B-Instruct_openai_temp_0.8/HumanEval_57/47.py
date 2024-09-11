```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    
    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    increasing = decreasing = True
    
    for i in range(1, len(l)):
        # Check if the list is increasing
        if l[i] < l[i-1]:
            increasing = False
        # Check if the list is decreasing
        elif l[i] > l[i-1]:
            decreasing = False
            
    return increasing or decreasing


# Test the function
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This script defines a function `monotonic` that takes a list of numbers as input and returns `True` if the list elements are monotonically increasing or decreasing, and `False` otherwise. It uses two flags, `increasing` and `decreasing`, to track whether the list is increasing or decreasing, respectively. The function iterates over the list, updating these flags based on the relative values of adjacent elements. Finally, it returns the logical OR of these flags, which will be `True` if the list is either increasing or decreasing. The script includes test cases to verify the function's correctness.