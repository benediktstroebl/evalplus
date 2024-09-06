```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [i + 1 for i in l]
    assert len(l) == n, f"Length of result list should be {n}, but got {len(l)}."
    assert all([i >= 1 for i in l]), f"List elements are not positive integers: {l}"
    return l
```