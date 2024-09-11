```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
    l (list): A list of numbers.

    Returns:
    bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    
    # Check if list is monotonically increasing
    is_increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    
    # Check if list is monotonically decreasing
    is_decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    
    # Return True if list is either increasing or decreasing
    return is_increasing or is_decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected: True
print(monotonic([1, 20, 4, 10]))  # Expected: False
print(monotonic([4, 1, 0, -10]))  # Expected: True
print(monotonic([1, 2, 2, 3]))  # Expected: True
print(monotonic([3, 2, 2, 1]))  # Expected: True
print(monotonic([1, 1, 1, 1]))  # Expected: True
print(monotonic([1, 1, 2, 3]))  # Expected: False
```

This script defines a function `monotonic` that checks if a given list of numbers is either monotonically increasing or decreasing. The test cases cover various scenarios, including lists of different sizes and different types of monotonicity.