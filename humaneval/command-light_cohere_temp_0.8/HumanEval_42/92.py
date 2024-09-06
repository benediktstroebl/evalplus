```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [i + 1 for i in l]
    assert len(result) == n, f"Length of result list should be {n}, but got {len(result)} instead."
    assert all(i >= n - 1 for i in result), f"Elements in result list should be non-negative, but got {result} instead."
    return result
```