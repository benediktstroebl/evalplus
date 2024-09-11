```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of integers.
    
    Returns:
    bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    
    # Check if the list is monotonically increasing
    increasing = all(l[i] <= l[i + 1] for i in range(len(l) - 1))
    
    # Check if the list is monotonically decreasing
    decreasing = all(l[i] >= l[i + 1] for i in range(len(l) - 1))
    
    # Return True if the list is either monotonically increasing or decreasing
    return increasing or decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([1, 1, 1, 1]))  # True
print(monotonic([10, 9, 8, 7]))  # True
print(monotonic([5, 4, 3, 2]))  # True
```

This script defines a function `monotonic(l)` that takes a list of integers as input and returns `True` if the list elements are monotonically increasing or decreasing, and `False` otherwise. The function uses the `all()` function in combination with generator expressions to check for both increasing and decreasing monotonicity. The test cases are provided at the end to demonstrate the function's behavior.