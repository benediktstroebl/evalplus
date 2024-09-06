```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) <= 1:
        return l[0]
    return (len(l) + 1) / 2.0 * (l[len(l) + 1) + l[-1])

# Test cases
median([3, 1, 2, 4, 5]) == 3.5
median([-10, 4, 6, 1000, 10, 20]) == 15.0
median([1, 2, 3, 4]) == 2.0
median([10, 11, 12, 13, 14, 3, 4, 5]) == 6.0
median([0.9, 1.6, 2.5, 3]) == 1.25
```