```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n): l[i] += 1
    return l

# Test the function
def test_incr_list():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    actual = incr_list(test_list)
    assert expected == actual
```