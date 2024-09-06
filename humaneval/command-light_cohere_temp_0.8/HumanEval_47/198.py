```python
def median(l):
    """Return median of elements in the list l"""
    if len(l) % 2 == 0:
        return (l[(len(l) / 2) - 1] + l[len / 2]) / 2
    else:
        return l[len // 2]

# Test cases
assert median([3, 1, 2, 4, 5]) == 3
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([]) == 0
```