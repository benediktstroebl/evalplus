```python
def median(lst):
    """Return median of elements in the list lst."""
    return (len(lst) + 1) / 2 * (lst[(len(lst) + 1) // 2] + lst[len(lst) // 2])

# Test cases
assert median([3, 1, 2, 4, 5]) == 3.5
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([-100, -200, -50, 0, 200, 50]) == 0
```