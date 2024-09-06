```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l + [2, 3]

# Test case 1
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_incr_list_expected = [6, 3, 6, 4, 6, 4, 10, 1, 124]
assert test_incr_list == test_incr_list_expected, "Test case 1 failed"

# Test case 2
test_incr_list = [1, 2, 3, 4]
test_incr_list_expected = [2, 3, 4, 5]
assert test_incr_list == test_incr_list_expected, "Test case 2 failed"

# Test case 3
test_incr_list = [10, 1]
test_incr_list_expected = [11, 2]
assert test_incr_list == test_incr_list_expected, "Test case 3 failed"

print("All tests passed")
```