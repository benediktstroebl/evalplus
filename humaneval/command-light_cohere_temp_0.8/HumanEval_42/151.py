```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [1]

# Test the function with a sample input
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_incr_list_result = incr_list(test_incr_list)

# Verify the output
assert test_incr_list_result == [6, 3, 6, 4, 6, 4, 4, 10, 1, 124]

# Another test with different input
test_incr_list_two = [5, 3, 5, 2, 3, 7]
test_incr_list_two_result = incr_list(test_incr_list_two)

# Verify the output again
assert test_incr_list_two_result == [8, 6, 8]
```