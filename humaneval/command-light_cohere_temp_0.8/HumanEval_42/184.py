```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [x + 1 for x in l]
    assert(all([x == l[x] for x in range(n)]))
    return l
```