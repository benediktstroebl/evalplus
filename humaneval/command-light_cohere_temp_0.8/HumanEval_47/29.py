```python
def median(l):
    """Return median of elements in the list l"""
    return (len(l) + 1) / 2 * sorted([int(x) for x in l])[int(len(l) / 2)]

# Test cases
assert median([3, 1, 2, 4, 5]) == 3.2
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([1, 2, 3, 4]) == 3.2
assert median([1, 2, 3, 4, 5]) == 5.0
assert median([10, 10, 10]) == 10.0
```