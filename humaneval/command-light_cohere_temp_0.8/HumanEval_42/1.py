```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l

# Test
def test_incr_list():
    l = incr_list([1, 2, 3])
    assert l == [2, 3, 4]
    l = incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    assert l == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Another test
def test_another_incr_list():
    l = incr_list([5, 6, 7])
    assert l == [6, 7]
```