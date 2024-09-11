```python
def monotonic(l: list) -> bool:
    """Return True is list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of numbers.
    
    Returns:
    bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    """
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This Python script defines a function `monotonic` that checks if a list of numbers is monotonically increasing or decreasing. It uses the `all` function with generator expressions to check if all consecutive pairs of numbers in the list are either non-decreasing (`l[i] <= l[i+1]`) or non-increasing (`l[i] >= l[i+1]`). If either of these conditions is true, the function returns `True`; otherwise, it returns `False`. The test cases at the end of the script demonstrate the function's behavior.