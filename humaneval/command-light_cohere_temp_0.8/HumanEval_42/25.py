```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    res = []
    for i in range(n):
        res.append(l[i] + 1)
    return res

# Test suite for function incr_list
def test_incr_list():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    got = incr_list(test_list)
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert got == expected
```