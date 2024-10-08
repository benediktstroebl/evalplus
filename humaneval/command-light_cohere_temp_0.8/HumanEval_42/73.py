```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [i+1 for i in l]
    return l

# Test
def test_incr_list():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    result = incr_list(test_list)
    assert list(result) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```