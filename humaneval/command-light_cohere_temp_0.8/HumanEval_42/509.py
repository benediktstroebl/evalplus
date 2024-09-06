```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [x + 1 for x in l]
    return l

# Test case 1
def test_incr_list():
    """Test the incr_list function with various input."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]  # True
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]  # True
    assert len(incr_list([10])) == 0  # False
```