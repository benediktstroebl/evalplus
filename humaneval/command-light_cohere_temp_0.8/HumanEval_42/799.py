```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    assert len(result) == n, "result list length mismatch"
    assert all(result[i] == i + 1 for i in range(n)), "Incorrect increment"
    return result
```