```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i + 1 for i in l]
    assert len(result) == n
    assert all(result) == l + [0]
    assert sorted(result) == [1, 2, 3, 4] + l
    return result
```