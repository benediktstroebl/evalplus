```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [i + 1 for i in l] + [n]
    assert len(result) == len(l) + 1
    return result

# Test the function with various inputs
# Test case 1
test_case1 = [1, 2, 3]
test_case2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_case3 = [6, 4, 6, 3, 4, 4, 6, 7, 8]
test_case4 = [100]
test_case5 = [1, 2, 3, 4, 5]

# Call the function and check the output against the test cases
result1 = incr_list(test_case1)
result2 = incr_list(test_case2)
result3 = incr_list(test_case3)
result4 = incr_list(test_case4)
result5 = incr_list(test_case5)

assert result1 == test_case1
assert result2 == test_case2
assert result3 == test_case3
assert result4 == test_case4
assert result5 == test_case5
```
The script defines a function `incr_list` that takes a list `l` as input and returns a new list with elements incremented by 1. The test cases include various lists with different elements and the `incr_list` function is called with each of them. The output is then compared against the test cases to ensure the function's correctness.