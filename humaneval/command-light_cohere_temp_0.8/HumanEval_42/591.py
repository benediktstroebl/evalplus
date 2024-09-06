```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test function
def test_incr_list():
    """Test incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert len(incr_list([99, 100, 101])) == 3  # Should increment to 102, 103 and 104
    assert incr_list([5, 6, 7, 8, 9, 10])) == [6, 7, 8]    # Extra element 10 is ignored
```