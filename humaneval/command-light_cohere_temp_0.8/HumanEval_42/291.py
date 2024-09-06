```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [i+1 for i in l]
    assert(all([i+1 == l[i] for i in range(n)]), "Assertions failed!")
    return l
```