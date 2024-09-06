```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(l[-1] + 1)
    return l

# Test function to check if incr_list works correctly
def test_incr_list():
    test_list = [1, 2, 3]
    expected = [2, 3, 4]
    actual = incr_list(test_list)
    assert actual == expected
```