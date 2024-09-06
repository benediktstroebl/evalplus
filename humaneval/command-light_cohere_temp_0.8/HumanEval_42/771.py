```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l]
    assert len(result) == n
    assert all(map(lambda x: x == i+1 for i, x in zip(result, l)))
    return result
```