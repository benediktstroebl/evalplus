```python
def median(lst):
    """Return median of elements in the list lst."""
    return (len(lst) + 1) / 2 * (sum(lst[:len(lst) // 2]) + sum(lst[-len(lst) - 1:]))

# Test suite
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

test_median()
```