```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [x + 1 for x in l]
    assert(all([x + 1 == l[0] for x in l]) )
    assert(all([x + 1 == l[-1] for x in l]) )
    assert(all([x + 1 == l[i] for i in range(n - 2)]))
    return l
```