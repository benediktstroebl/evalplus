```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test case 1
def test_incr_list():
    """Test the incr_list function with a list containing various elements."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]  # Should return [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]  # Should return [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 2
def test_incr_list2():
    """Test the incr_list function with an empty list."""
    assert incr_list([]) == []  # Should return []
```
The test_incr_list function contains two test cases that verify the correctness of the incr_list function. The test_incr_list2 function tests the incr_list function with an empty list.