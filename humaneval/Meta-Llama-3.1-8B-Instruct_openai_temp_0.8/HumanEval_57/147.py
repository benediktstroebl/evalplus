```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    
    # Check if the list is empty
    if len(l) == 0:
        return True
    
    # Check if the list has only one element
    if len(l) == 1:
        return True
    
    # Check if the list is monotonically increasing
    increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    
    # Check if the list is monotonically decreasing
    decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    
    # Return True if the list is monotonically increasing or decreasing, False otherwise
    return increasing or decreasing

# Test the function
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
print(monotonic([]))  # Expected output: True
print(monotonic([5]))  # Expected output: True
```

This script defines a function `monotonic` that checks if a list of numbers is monotonically increasing or decreasing. It uses the `all` function in combination with generator expressions to check if the list is increasing or decreasing. If the list has one or zero elements, the function returns `True` because these lists are considered to be monotonically increasing or decreasing. The function is then tested with several examples.