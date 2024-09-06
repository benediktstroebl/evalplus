```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [1]

# Test drive function
def test_incr_list():
    l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert l == incr_list(l), "incorrect result"

# Run tests
test_incr_list()
```