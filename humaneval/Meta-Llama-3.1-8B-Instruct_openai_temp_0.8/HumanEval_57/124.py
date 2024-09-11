```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that takes a list of numbers as input. It uses the `all` function with a generator expression to check if all pair of adjacent elements in the list are monotonically increasing (`l[i] <= l[i+1]`) or decreasing (`l[i] >= l[i+1]`). If either condition is met, the function returns `True`, otherwise it returns `False`. The test cases at the end demonstrate the function's usage.