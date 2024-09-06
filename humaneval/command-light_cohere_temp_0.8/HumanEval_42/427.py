```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [x + 1 for x in l]
    assert(all([x + 1 == l[0] for x in l]) and all([x == l[-1] for x in l]), "Test 1 failed"
    assert(len(l) == n, "Test 2 failed")
    return l
```