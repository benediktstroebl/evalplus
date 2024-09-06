```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l[:] + [2]

# Test suite for function
def test_incr_list():
    actual = incr_list([1, 2, 3])
    expected = [2, 3, 4]
    assert actual == expected
```