```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): A list of integers.
    
    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    # Check if list is monotonically increasing
    increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    
    # Check if list is monotonically decreasing
    decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    
    # Return True if list is either increasing or decreasing
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script uses the `all()` function in combination with a generator expression to check if the list is either monotonically increasing or decreasing. The `all()` function returns `True` if all elements in the given iterable are true. If at least one element is false, it returns `False`.