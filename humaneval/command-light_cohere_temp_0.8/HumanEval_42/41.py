```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l[:] = [i+1 for i in l]
    return l

# Test cases for incr_list function
def test_incr_list():
    """Test the incr_list function with various input."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert not incr_list([]) == []
    assert not incr_list([5, 6, 7]) == [5, 6, 7]
    assert incr_list([2, 1, 1]) == [3, 2, 2]
```