```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [x + 1 for x in l]
    assert(all(x == l[0] for x in l)), "Assertions failed"
    return l
```