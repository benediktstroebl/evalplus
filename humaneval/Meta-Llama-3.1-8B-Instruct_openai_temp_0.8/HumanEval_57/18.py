```python
def monotonic(lst):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    
    # Check if the list is empty
    if len(lst) < 2:
        return True
    
    # Check if the list is increasing
    increasing = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    
    # Check if the list is decreasing
    decreasing = all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
    
    # Return True if the list is either increasing or decreasing
    return increasing or decreasing

# Example usage:
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This script defines a function `monotonic` that checks if the elements of a list are monotonically increasing or decreasing. It returns `True` if the list meets either condition and `False` otherwise. The function uses the built-in `all` function with a generator expression to check if the list satisfies the increasing or decreasing condition. If the list has less than two elements, the function returns `True` because a list with one element is trivially monotonic.