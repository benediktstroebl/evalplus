```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [i+1 for i in l]
    assert(all(i>=0 for i in l)), "List should not contain negative numbers"
    assert(len(l)==n), "List length should match function parameter length"
    return l

# Test suite
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4], "Incorrect return value"
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124], "Incorrect return value"
```