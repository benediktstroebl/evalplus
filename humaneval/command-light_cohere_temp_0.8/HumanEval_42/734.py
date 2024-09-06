```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l.append(l[-1]+1)
    return l

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_out1 = incr_list(test_case1)
assert test_out1 == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 2
test_case2 = [1, 2, 3]
test_out2 = incr_list(test_case2)
assert test_out2 == [2, 3, 4]

# Test case 3
test_case3 = [5, 3, 5, 2, 3, 3, 9, 0]
test_out3 = incr_list(test_case3)
assert test_out3 == [6, 4, 6, 3, 4, 4, 10]
```

This script defines a function `incr_list` that takes a list `l` as input and returns a new list with the last element of the original list incremented by 1. The test cases provide sample lists and the function's output, then compare the two to ensure the function is working correctly.