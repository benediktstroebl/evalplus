```python
def median(l: list):
    """Return median of elements in the list l.
    m = len(l)
    if m % 2 == 1:
        return (l[int((m - 1) / 2)] + l[int((m - 2) / 2)]) / 2
    else:
        return l[(int(m / 2) - 1)]

# Test
def test_median():
    return median([3, 1, 2, 4, 5]) == 3.0
```