```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    res = []
    for i in range(n):
        res.append(l[i] + 1)
    return res

# Test function
def test_incr_list():
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    res = incr_list(lst)
    print("Result:", res)
    assert res == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```