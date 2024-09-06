```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1
test_case1 = [1, 2, 3]
test_result1 = incr_list(test_case1)
assert test_result1 == [2, 3, 4]

# Test case 2
test_case2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result2 = incr_list(test_case2)
assert test_result2 == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
The above Python script defines a function `incr_list` that takes a list `l` as an argument and returns a new list with elements incremented by 1. 

The `test_case1` and `test_case2` are two sets of elements. Both are passed to the function `incr_list` and the resulting lists are compared with the expected results using `assert` statements. 

This script ensures that the `incr_list` function works as expected.