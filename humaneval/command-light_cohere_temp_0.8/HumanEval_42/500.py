```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test the function with known good inputs
test_incr_list = [1, 2, 3]
test_incr_list_copy = copy.deepcopy(test_incr_list)
assert incr_list(test_incr_list) == [2, 3, 4]
assert incr_list(test_incr_list_copy) == [2, 3, 4]

# Test the function with known bad inputs
try:
    test_err_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert incr_list(test_err_list) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert False
except AssertionError as e:
    print("Error:",e)
```