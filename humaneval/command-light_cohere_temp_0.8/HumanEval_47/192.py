```python
def median(l: list):
    """Return median of elements in the list l."""
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]
# Tests
def test_median():
    """Function to test the median function."""
    lst = [-10, 4, 6, 1000, 10, 20, 2, 20, 3]
    assert median(lst) == 3.0, "Wrong median value."
```