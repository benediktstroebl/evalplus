```python
def median(lst):
    """Return median of elements in the list lst"""
    return (len(lst) + 1) / 2 * (sum(lst) / len(lst))

# Test case 1
assert median([3, 1, 2, 4, 5]) == 3.6

# Test case 2
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

# Test case 3
assert median([10, 20, 30, 10, 40]) == (25 / 4) * (40 + 10)
```