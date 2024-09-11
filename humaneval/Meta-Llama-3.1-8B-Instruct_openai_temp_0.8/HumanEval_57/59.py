```python
def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    
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

In this script, the `monotonic` function takes a list `l` as input and returns `True` if the list elements are monotonically increasing or decreasing, and `False` otherwise. The function uses the `all` function with a generator expression to check for both increasing and decreasing conditions. The test cases are then executed to verify the function's correctness.