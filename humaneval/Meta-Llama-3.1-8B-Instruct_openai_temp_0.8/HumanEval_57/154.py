```python
def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    
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
    
    # Check if list is empty
    if len(l) < 2:
        return True
    
    # Check if list elements are monotonically increasing or decreasing
    increasing = decreasing = True
    
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            decreasing = False
        elif l[i] > l[i + 1]:
            increasing = False
    
    return increasing or decreasing

# Test the function
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
print(monotonic([1, 1, 1, 1]))    # Expected output: True
print(monotonic([]))              # Expected output: True
```

This Python script defines a function `monotonic` that checks if the elements of a given list are monotonically increasing or decreasing. It iterates over the list and checks if each element is greater than or equal to the previous one (for increasing order) or less than or equal to the previous one (for decreasing order). If the list is empty or has only one element, the function returns `True`. Finally, the script includes some test cases to verify the function's correctness.