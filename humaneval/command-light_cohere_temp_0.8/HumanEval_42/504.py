```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    res = [0] * (n+1)
    res[1:] = 1
    for i in range(2, n+1):
        res[i] = l[i-1] + 1
    return res
def test_incr():
    """Test incr_list function."""
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    got = incr_list(lst)
    assert expected == got
```