```python
def median(l):
    """Return median of elements in the list l.
    if len(l) < 1:
        return None  # Return None for empty list
    m = len(l) // 2 + 1
    if len(l) % 2 == 0:
        return (l[m - 1] + l[m]) / 2
    else:
        return l[m]

# Test cases
median([3, 1, 2, 4, 5])  # Expected: 3.5
median([-10, 4, 6, 1000, 10, 20])  # Expected: 15.0
median([5, 10, -20, -30, 80, 60, 100])  # Expected: 50.0
median([1, 2, 3, 4, 5, 6])  # Expected: 3.5
```