```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of elements to check for monotonicity.
    
    Returns:
    bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    # Check if the list is empty
    if len(l) == 0:
        return True
    
    # Check if the list is monotonically increasing
    increasing = all(x <= y for x, y in zip(l, l[1:]))
    
    # Check if the list is monotonically decreasing
    decreasing = all(x >= y for x, y in zip(l, l[1:]))
    
    # Return True if the list is either increasing or decreasing
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([]))  # True
print(monotonic([1]))  # True
```

This script defines a function `monotonic` that takes a list `l` as input and returns `True` if the list elements are monotonically increasing or decreasing, and `False` otherwise. The function uses the `all` function with generator expressions to check if the list elements are monotonically increasing or decreasing. The test cases at the end validate the function's behavior for different inputs.