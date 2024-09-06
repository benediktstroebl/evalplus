```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    assert len(result) == n
    assert all(result[i] == i + 1 for i in range(n))
    return result

# Test suite with additional failures
def test_incr_list():
    try:
        l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
        result = incr_list(l)
        assert len(result) == 6
        assert result[0] == 6
        assert result[1] ==  3
        assert result[4] == 6
        assert result[5] ==  4
    except:
        assert False
```