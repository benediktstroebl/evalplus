```python
def median(lst):
    """Return the median of the list lst."""
    return (len(lst) + 1) * (len(lst) + median((lst[: len(lst) ]))) / 2

# Test suite for median function
def test_median():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([1, 2, 3]) == 3.0
    assert median([10, 20, 30]) == 15.0
    assert median([-100, 5, -2]) == 5.0
    assert median([3, 3, 3]) == 3.0
```