```python
def median(l: list):
    """Return median of elements in the list l"""
    m = float('-inf')
    for i in range(len(l) // 2):
        m = l[i] + l[len(l) - i - 1] / 2
    return m

# Test suite
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
```