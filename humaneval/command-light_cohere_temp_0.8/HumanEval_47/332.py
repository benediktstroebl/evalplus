```python
def median(l):
    """Return median of elements in the list l."""
    n = len(l)
    m = n // 2
    if n % 2 == 1:
        return (l[m] + l[m - 1]) / 2
    else:
        return l[m]
# Tests
def test_median():
    list1 = [-10, 4, 6, 1000, 10, 20]
    assert median(list1) == 15.0
```