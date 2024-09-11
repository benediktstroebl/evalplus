```python
def monotonic(lst: list):
    """Return True is list elements are monotonically increasing or decreasing.
    
    Args:
    lst (list): A list of numbers.
    
    Returns:
    bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    
    Examples:
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    return len(lst) == len(set(lst)) or (all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) or all(lst[i] >= lst[i+1] for i in range(len(lst)-1)))

# Test the function
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that checks if a list of numbers is monotonically increasing or decreasing. It uses the property that a list with no duplicates (checked with `len(lst) == len(set(lst))`) can only fail the monotonicity test if it is neither increasing nor decreasing. Otherwise, it checks both conditions with generator expressions (`all(lst[i] <= lst[i+1] for i in range(len(lst)-1))` and `all(lst[i] >= lst[i+1] for i in range(len(lst)-1))`) to see if the list is either increasing or decreasing. If either condition is met, the function returns True; otherwise, it returns False.