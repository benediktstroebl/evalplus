### Monotonic List Check
#### Python Script
```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    
    # Check if the list is empty
    if not l:
        return True  # An empty list is considered monotonically increasing or decreasing
    
    # Check if the list has only one element
    if len(l) == 1:
        return True  # A list with one element is considered monotonically increasing or decreasing
    
    # Check if the list is monotonically increasing
    increasing = all(x <= y for x, y in zip(l, l[1:]))
    
    # Check if the list is monotonically decreasing
    decreasing = all(x >= y for x, y in zip(l, l[1:]))
    
    # Return True if the list is monotonically increasing or decreasing
    return increasing or decreasing

# Example usage:
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```
This script defines a function `monotonic` that checks if a given list of numbers is monotonically increasing or decreasing. It returns `True` if the list meets this condition and `False` otherwise. The example usage section demonstrates the function's behavior with various inputs.