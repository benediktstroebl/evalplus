```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [x+1 for x in l]
    return result

# Test case 1
test_case1 = [1, 2, 3]
test_case1_expected = [2, 3, 4]
result = incr_list(test_case1)
assert list(result) == test_case1_expected, "Test case 1 failed"

# Test case 2
test_case2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_case2_expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
result = incr_list(test_case2)
assert list(result) == test_case2_expected, "Test case 2 failed"

# Test case 3
test_case3 = [20, 80]
test_case3_expected = [21, 81]
result = incr_list(test_case3)
assert list(result) == test_case3_expected, "Test case 3 failed"

print("All tests passed!")
```