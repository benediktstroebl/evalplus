```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    assert len(result) == n
    assert all(x >= 0 for x in result)
    assert all(x <= n for x in result)
    return result
```