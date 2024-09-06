```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) % 2 == 0:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
    else:
        return l[len(l) // 2]

# Test cases
assert median([3, 1, 2, 4, 5]) == 3
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([3, -3, 4, -4]) == 3
assert median([8, 9, 2, 1]) == 5.0
assert median([1, 2, 3, 4, 5]) == 4
```