```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l]
    assert len(result) == n
    assert all(map(lambda x: x >= 0, result))
    assert all(map(lambda x: x <= n, result))
    return result
```