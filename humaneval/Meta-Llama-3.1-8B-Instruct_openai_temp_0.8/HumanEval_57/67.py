```python
def monotonic(lst: list) -> bool:
    """Return True if list elements are monotonically increasing or decreasing."""
    return (all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) 
            or all(lst[i] >= lst[i+1] for i in range(len(lst)-1)))

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that checks if the elements of a list are monotonically increasing or decreasing. It uses the `all` function with a generator expression to check both conditions: if all elements are less than or equal to the next one, or if all elements are greater than or equal to the next one. If either condition is true, the function returns `True`; otherwise, it returns `False`. The test cases at the end demonstrate the function's behavior.