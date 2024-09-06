```python
def median(l: list):
    """Return median of elements in the list l.
    assert len(l) > 1,
    mid = len(l) // 2
    if l[mid] > l[mid + 1]:
        return (l[mid] + l[mid + 1]) / 2
    else:
        return l[mid]

# Test cases
test_median = median([3, 1, 2, 4, 5])
assert test_median == 3
test_median = median([-10, 4, 6, 1000, 10, 20])
assert test_median == 15.0
```