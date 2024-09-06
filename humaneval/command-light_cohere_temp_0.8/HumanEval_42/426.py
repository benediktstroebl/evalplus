```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    l = [x + 1 for x in l]
    assert len(l) == n + 1, f"Length mismatch: {l}"
    assert all(x == n for x in zip(l, range(n))), f"Element mismatch: {l}"
    return l
```