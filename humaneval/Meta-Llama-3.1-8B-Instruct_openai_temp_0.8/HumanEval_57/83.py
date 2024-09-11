```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    lst: A list of elements
    
    Returns:
    True if the list is monotonically increasing or decreasing, False otherwise
    """
    
    # Check if the list is empty or contains only one element
    if len(lst) <= 1:
        return True
    
    # Check if the list is increasing
    increasing = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    
    # Check if the list is decreasing
    decreasing = all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
    
    # Return True if the list is either increasing or decreasing
    return increasing or decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
print(monotonic([1, 1, 1, 1]))  # Expected output: True
print(monotonic([]))  # Expected output: True
print(monotonic([1]))  # Expected output: True
```

This script uses the `all()` function with a generator expression to check if the list is either increasing or decreasing. If all elements in the list are less than or equal to the next element in both cases, then the list is either increasing or decreasing. The `or` operator is used to combine the two conditions.