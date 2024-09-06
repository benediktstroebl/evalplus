```python
def median(lst):
    """Return median of elements in the list lst."""
    return (len(lst) + 1) * (sum((lst[: len // 2])) / 2

# Test cases for the median function
assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([1, 2, 3, 4, 5]) == 5.0
assert median([10, 20, 30, 40, 50]) == 30.0
assert median([1, 2, 3, 4]) == 3.0
assert median([5, 4, 3, 6, 7]) == 5.0
```
This code defines a median function and provides corresponding test cases to ensure the function's correctness.