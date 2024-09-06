```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l]
    assert len(result) == n
    assert all(map(lambda x: x == x+1, result))
    return result

# Test code
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
```