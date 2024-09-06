```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i + 1 for i in l]
    assert len(result) == n
    assert all(result[i] == i + 1 for i in range(n))
    return result
```