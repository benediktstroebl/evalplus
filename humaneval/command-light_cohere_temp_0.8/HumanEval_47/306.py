```python
def median(l):
    """Return median of elements in the list l.
    m = 0
    if len(l) <= 1:
        return float('inf')
    return (l[len(l) // 2] + l[(len(l) + 1) // 2]) / 2.0
```

# Test suite
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([]) == float('inf')
```