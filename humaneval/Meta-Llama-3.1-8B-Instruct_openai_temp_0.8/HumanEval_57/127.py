```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of numbers.
    
    Returns:
    bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    
    # Check if the list has less than 2 elements
    if len(l) < 2:
        return True  # A list with less than 2 elements is always monotonically increasing/decreasing
    
    # Check if the list is monotonically increasing
    is_increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    
    # Check if the list is monotonically decreasing
    is_decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    
    # The list is monotonically increasing or decreasing if it is either increasing or decreasing
    return is_increasing or is_decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that checks if the elements of a list are monotonically increasing or decreasing. It uses list comprehensions to check for both increasing and decreasing sequences and returns True if either condition is met. The function is then tested with the provided example use cases.