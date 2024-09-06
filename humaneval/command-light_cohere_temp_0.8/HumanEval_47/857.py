```python
def median(l: list):
    """Return median of elements in the list l."""
    n = len(l)
    m = n // 2 + 1
    if n % 2 == 0:
        return (l[m-1] + l[m]) / 2
    else:
        return l[m]

# Test the function
def test_median():
    # Input list with positive and negative numbers and mixed cases
    l = [-10, 4, 6, 1000, 10, 20, 2, -5, 0, 5, 20]
    assert median(l) == 15.0

# Test list with all positive numbers
l = [10, 10, 10, 10]
assert median(l) == 10

# Test list with all negative numbers
l = [-10, -10, -10]
assert median(l) == 0
```