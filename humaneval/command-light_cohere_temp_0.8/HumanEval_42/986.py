```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(l[-1] + 1)
    return l

# Test the function with a sample input
test_incr_list = [1, 2, 3]
test_incr_list_res = incr_list(test_incr_list)
assert test_incr_list_res == [2, 3, 4]

# Test the function again with a longer list
test_long_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_long_list_res = incr_list(test_long_list)
assert test_long_list_res == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```