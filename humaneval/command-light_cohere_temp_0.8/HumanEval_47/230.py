```python
def median(lst):
    """Return median of elements in the list lst."""
    return (lst[(len(lst) + 1) // 2] + lst[len(lst) // 2]) / 2

# Tests
assert median([3, 1, 2, 4, 5]) == 3.2
assert median([-10, 4, 6, 1000, 10, 20]) == 15
```