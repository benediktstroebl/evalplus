```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    return result

# Test case 1
test_case_1 = [1, 2, 3]
test_result_1 = incr_list(test_case_1)
assert list(test_result_1) == [2, 3, 4]

# Test case 2
test_case_2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result_2 = incr_list(test_case_2)
assert list(test_result_2) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```