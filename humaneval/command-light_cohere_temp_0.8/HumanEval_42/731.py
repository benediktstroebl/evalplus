```python
def incr_list(lst):
    """Return list with elements incremented by 1."""
    lst[:] = [1] + lst
    return lst

# Test the function with a list of strings
test_incr_list = []
test_incr_list.push_str = lambda x:test_incr_list.push_str([5, 3, 5, 2, 3, 3, 9, 0, 'Hello'])
test_incr_list.push_str()
def test_incr_list():
    """Test the incr_list function."""
    assert incr_list(test_incr_list) == test_incr_list.push_str([1, 2, 3])
    assert incr_list(test_incr_list) == [2, 3, 4]
    assert incr_list(test_incr_list) == [2, 3, 4, 0]
    assert incr_list(test_incr_list) == [6, 4, 6, 3, 4, 4]
    assert incr_list(test_incr_list) == [6, 4, 10, 1, 124]

# Run the test function
test_incr_list()
```