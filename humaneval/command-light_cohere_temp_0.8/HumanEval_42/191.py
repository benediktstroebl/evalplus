```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    assert len(result) == n
    assert all(result) >= n
    assert sum(result) == n * (n + 1) // 2
    return result

# Test code
def test_incr_list():
    input_list = [5, 3, 5, 2, 3, 3]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    result = incr_list(input_list)
    assert result == expected
```