```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of elements.
    
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

This Python script defines a function `monotonic` that checks if the elements of a list are monotonically increasing or decreasing. The function uses the `all` function in combination with a generator expression to check if all elements in the list are less than or equal to the next element (for increasing) or greater than or equal to the next element (for decreasing). The test cases at the end of the script demonstrate the function's usage.