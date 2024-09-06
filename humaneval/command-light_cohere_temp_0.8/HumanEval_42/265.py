```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [i+1 for i in l]
    assert len(l) == n + 1, f"List length mismatch: {l}"
    return l
```