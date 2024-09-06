```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    res = [x+1 for x in l] + l
    return res

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert incr_list(test_case1) == [6, 3, 6, 4, 6, 4, 4, 10, 1, 124]

# Test case 2
test_case2 = [5, 3, 2], [6, 3, 5]
assert incr_list(test_case2) == [6, 7, 3]

# Test case 3
test_case3 = [1, 2, 3], [4, 5, 6]
assert incr_list(test_case3) == [3, 5, 6]
```