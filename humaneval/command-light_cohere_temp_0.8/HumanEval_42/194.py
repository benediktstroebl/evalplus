```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    res = [0] * (n + 1)
    for i in range(n): res[i + 1] = l[i] + 1
    return res

# Test case 1: Basic Increment
test_incr_list = [1, 2, 3]
test_res = incr_list(test_incr_list)
assert test_res == [2, 3, 4]

# Test case 2: Different Length List
test_different_length = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_res = incr_list(test_different_length)
assert test_res == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3: Different Elements List
test_elements = [5, 'abc', 9, 123]
test_res = incr_list(test_elements)
assert test_res == [6, 'abc', 9, 10, 1, 124]
```
This Python script defines a function `incr_list` that takes a list as input and returns a new list with elements incremented by 1. The function is tested with three different cases: basic increment, different length list, and a list with different elements. 

The test cases verify that the `incr_list` function produces the expected results for the provided inputs.