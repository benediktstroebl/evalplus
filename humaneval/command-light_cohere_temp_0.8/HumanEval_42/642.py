```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l] + l
    return result

# Test the function with various inputs
test_list = [1, 2, 3]
test_result = incr_list(test_list)
assert test_result == [2, 3, 4]

test_empty_list = []
test_result_empty = incr_list(test_empty_list)
assert test_result_empty == []

test_list_large = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result_large = incr_list(test_list_large)
assert test_result_large == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This script defines a function `incr_list` that returns a new list with list elements incremented by 1. The test suite consists of several input scenarios to ensure the function works correctly with different list contents.