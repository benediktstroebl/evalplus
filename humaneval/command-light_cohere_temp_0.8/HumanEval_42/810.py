```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1: Basic Incrementation
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_incr_list)
assert list(result) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 2: Clearing the initial value
test_incr_list = [5, 3, 5, 2, 3, 3]
result = incr_list(test_incr_list)
assert list(result) == [6, 4, 6]

# Test case 3: Backward increment
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_incr_list, -1)
assert list(result) == [5, 3, 5, 2, 3, 3, 8, 0, 321]

# Test case 4: Complex list initialization
test_list = [[x + 1 for x in range(10)]
result = incr_list(test_list)
assert list(result) == [10, 11, 12, 13, 14, 15, 16, 17, 18]
```

This script provides a self-contained function `incr_list` that takes a list as input and returns a new list with elements incremented by 1. The test cases cover basic increment, clearing the initial value, backward increment, and creating a list from a range.