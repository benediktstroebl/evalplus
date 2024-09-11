```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    is_increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    is_decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    
    return is_increasing or is_decreasing

# Test cases
if monotonic([1, 2, 4, 20]):
    print("Test case 1 passed")
if not monotonic([1, 20, 4, 10]):
    print("Test case 2 passed")
if monotonic([4, 1, 0, -10]):
    print("Test case 3 passed")
```

This script uses a list comprehension to check two conditions: whether the list is monotonically increasing (`is_increasing`) and whether the list is monotonically decreasing (`is_decreasing`). The `all()` function is used to ensure that all elements in the list satisfy the condition. The function returns `True` if either condition is met, and `False` otherwise.