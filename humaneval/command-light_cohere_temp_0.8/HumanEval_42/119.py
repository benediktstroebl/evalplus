```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test function to check the implementation
def test_incr_list():
    """Return list with elements decremented and then incremented."""
    l = [1, 2, 3]
    original = l[:] + [0]
    expected = [2, 3, 4] + l
    returned = incr_list(original)
    assert original == returned
    assert expected == returned
```