```python
def median(l: list):
    """Return median of elements in the list l.
    return sorted(l)[len(l) // 2]

# Test
def test_median():
    l = [-10, 4, 6, 1000, 10, 20]
    assert median(l) == 15.0

# Another test case
l = [1, 2, 3, 4, 5]
test_median()
```