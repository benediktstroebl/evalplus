```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l[:] + [1]

# Test case
def test_incr_list():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    actual = incr_list(test_list)
    assert actual == expected
```