```python
def median(l: list):
    """Return median of elements in the list l."""
    assert len(l) > 1, "List must have more than one element"
    m = l[len(l)//2]
    assert abs(m - (l[0] + l[-1])/2) < 1e-5, "Not sorted"
    return m

# Test code
def test_median():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
```