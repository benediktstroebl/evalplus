```python
def median(l):
    """Return median of elements in the list l.
    if len(l) < 1:
        raise ValueError("List must contain at least two elements.")
    if len(l) % 2 == 0:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    else:
        return l[len(l) // 2]

# Test suite for the median function
def test_median():
    test_list = [1, 2, 3, 4, 5]
    assert median(test_list) == 3.0
    test_list = [4, 5, -10, 6, -20]
    assert median(test_list) == -10.0
test_list = [5, -5, -20, -15]
    assert median(test_list) == -15.0
test_list = [1, 20, 10, 40, 50]
    assert median(test_list) == 10.0
```