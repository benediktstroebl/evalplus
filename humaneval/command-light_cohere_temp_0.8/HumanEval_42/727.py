```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(l[-1] + 1)
    return l

# Test case 1
test_case1 = [1, 2, 3]
result_case1 = incr_list(test_case1)
assert result_case1 == [2, 3, 4]

# Test case 2
test_case2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result_case2 = incr_list(test_case2)
assert result_case2 == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3 (negative increment)
test_case3 = [5, 3, 5, 2, 3, 3, -9, 0, 123]
result_case3 = incr_list(test_case3)
assert result_case3 == [6, 4, 6, 3, 4, 4, -1, 2, 123]
```