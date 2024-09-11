```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing."""
    is_increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    is_decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    return is_increasing or is_decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([1, 3, 2, 4]))  # False
print(monotonic([1, 1, 1, 1]))  # True
```

This script defines a function `monotonic` that checks if a list is monotonically increasing or decreasing by comparing each element with its successor. The `all` function checks if all elements in the generator expression are `True`. If both the list is increasing and decreasing, the function returns `True`. If the list is neither increasing nor decreasing, the function returns `False`. The test cases at the end demonstrate the function's behavior on different inputs.