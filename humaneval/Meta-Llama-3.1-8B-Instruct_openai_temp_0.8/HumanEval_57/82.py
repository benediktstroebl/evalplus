```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    
    # Check if the list is monotonically increasing
    is_increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    
    # Check if the list is monotonically decreasing
    is_decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    
    # Return True if the list is either monotonically increasing or decreasing
    return is_increasing or is_decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

In this script, we define a function `monotonic` that takes a list `l` as input. We use the `all` function with a generator expression to check if the list is monotonically increasing or decreasing. The function returns `True` if the list is either monotonically increasing or decreasing, and `False` otherwise. We include test cases to demonstrate the function's behavior.