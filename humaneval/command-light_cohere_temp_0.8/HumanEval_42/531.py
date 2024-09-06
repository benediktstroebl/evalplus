```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    assert(all(x == result[0] for x in l)), "AssertionError: List not updated properly!"
    return result
```