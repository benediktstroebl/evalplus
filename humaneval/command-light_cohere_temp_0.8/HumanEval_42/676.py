```python
def incr_list(lst):
    """Return list with elements incremented by 1."""
    new_lst = [x + 1 for x in lst]
    return new_lst

# Test
def test_incr_list():
    """Test the incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```