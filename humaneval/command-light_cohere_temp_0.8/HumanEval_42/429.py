```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l]
    return result

# Test the function with a list of 5 elements
test_list = [5, 3, 5, 2, 3]
test_result = incr_list(test_list)
assert test_result == [6, 4, 6, 3, 4]

# Test the function with a list of elements to be incremented by 3
test_other_list = [5, 3, 5, 2, 3, 3]
test_result_other = incr_list(test_other_list)
assert test_result_other == [8, 6, 9, 5, 6]
```