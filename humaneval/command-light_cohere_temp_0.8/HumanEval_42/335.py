```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n):
        l[i] = l[i] + 1
    return l

# Test function
def test_incr_list():
    lst = [1, 2, 3]
    expected = [2, 3, 4]
    result = incr_list(lst)
    assert result == expected
```