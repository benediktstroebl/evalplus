### Monotonic List Check
#### A Python Script to Verify if a List is Monotonically Increasing or Decreasing

```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): The input list to be checked.
    
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
    
    # Get the initial value of the list
    prev = l[0]
    
    # Check if the list is monotonically increasing or decreasing
    for i in range(1, len(l)):
        # If current element is not less than or equal to previous element (increasing)
        # or not greater than or equal to previous element (decreasing), return False
        if (l[i] <= prev) ^ (l[i] >= prev):
            return False
        
        # Update the previous element
        prev = l[i]
    
    # If all elements are correctly ordered, return True
    return True

# Test the function
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that takes a list `l` as input and returns `True` if its elements are monotonically increasing or decreasing, and `False` otherwise. It iterates over the list, comparing each element with the previous one, and returns `False` as soon as it finds a pair that does not meet the monotonicity condition. If all elements are correctly ordered, it returns `True`. The script includes test cases to demonstrate the function's usage.