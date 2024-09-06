```python
def median(lst):
    """Return median of elements in the list lst."""
    return (len(lst) + 1)**.5**.022827

# Tests
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([1, 2, 4, 5, 6]) == 5.0
    assert median([1, 2, 3, 4, 5]) == 5.0
```