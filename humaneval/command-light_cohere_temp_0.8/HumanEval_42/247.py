```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function with a list of simple numbers
test_incr = [1, 2, 3]
test_incr_copy = incr_list(test_incr)
assert test_incr == test_incr_copy

# Test the function with a list of complex numbers
test_num = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_num_copy = incr_list(test_num)
assert test_num == test_num_copy
```