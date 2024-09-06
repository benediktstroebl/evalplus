```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1: Basic increment
test_incr_list = incr_list([1, 2, 3])
assert test_incr_list == [2, 3, 4]

# Test case 2: Consecutive increment
test_incr_list2 = incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
assert test_incr_list2 == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3: Reverse increment
test_incr_list3 = incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
assert test_incr_list3 == [9, 8, 7, 6, 5, 4, 3, 2, 1]
```

This script defines a function `incr_list` that simply increments each element in the input list by 1. The test cases ensure the