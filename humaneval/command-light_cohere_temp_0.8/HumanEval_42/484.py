```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    res = [x+1 for x in l] + l
    return res

# Test the function with a list of known values
# Test case 1
test_list1 = [1, 2, 3]
test_result1 = incr_list(test_list1)
assert test_result1 == [2, 3, 4]

# Test case 2
test_list2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result2 = incr_list(test_list2)
assert test_result2 == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
The code defines a function `incr_list` that takes a list as input and returns a new list with elements incremented by 1. The test cases use the general lists with known values, and the `incr_list` function is applied to these lists to validate its correctness. The test results are compared against the expected values.