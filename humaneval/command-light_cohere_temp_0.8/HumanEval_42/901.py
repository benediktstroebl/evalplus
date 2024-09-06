```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    l.append(l[n] + 1)
    return l

# Test function to check if incr_list works
def test_incr_list():
    l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    actual = incr_list(l)
    assert expected == actual
```