```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    return result

# Test function
def test_incr_list():
    """Test incr_list function."""
    assert list(incr_list([1, 2, 3]) == [2, 3, 4])
    assert list(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 4, 10, 1, 124])
    assert len(list(incr_list([]))) == 0
```