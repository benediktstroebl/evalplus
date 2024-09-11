```python
def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    # Check if the list is increasing
    increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    
    # Check if the list is decreasing
    decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    
    # Return True if the list is either increasing or decreasing
    return increasing or decreasing


# Test the function
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that takes a list as input and returns `True` if the elements in the list are monotonically increasing or decreasing, and `False` otherwise. It uses Python's built-in `all` function in combination with a generator expression to check if the list is either increasing or decreasing. The test cases are then executed to demonstrate the function's behavior.