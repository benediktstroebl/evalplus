```python
def median(l):
    """Return median of elements in the list l."""
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]

# Test suite for the median function
def test_median():
    lst = [-10, 4, 6, 1000, 10, 20, 2, 3, 1]
    assert median(lst) == 3.0
    assert median([4, 5]) == 5.0
    assert median([1]) == 1.0

# Driver code to run the test suite
test_median()()
```