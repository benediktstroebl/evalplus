```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1
test_1 = [1, 2, 3]
test_result_1 = incr_list(test_1)
assert test_result_1 == [2, 3, 4]

# Test case 2
test_2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result_2 = incr_list(test_2)
assert test_result_2 == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3 (Should fail, list index out of range)
test_3 = [1, 2, 3, 4, 5, 6]
try:
    test_result_3 = incr_list(test_3)
    assert False, "Should have raised IndexError"
except IndexError:
    pass
```