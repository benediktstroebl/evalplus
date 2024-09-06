```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l[:] = [x+1 for x in l]
    return l

# Test function to check if the incr_list function works correctly
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4] # Passes the test!

# Test set with various inputs to check the function behavior
test_set = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_set2 = [10, 20, 30]

test_incr_list()
test_incr_list(test_set)
test_incr_list(test_set2)
 ```