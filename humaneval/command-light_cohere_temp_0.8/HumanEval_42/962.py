```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i + 1 for i in l]
    assert len(result) == n, "Result list length did not match input list length."
    assert all(result[i] == i + 1 for i in range(n)), "Incorrect result list"
    return result
```