```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1: basic list
test_case1 = [1, 2, 3]
result_case1 = incr_list(test_case1)
assert result_case1 == [2, 3, 4]

# Test case 2: list with duplicate elements
test_case2 = [5, 3, 5, 2, 3, 3]
result_case2 = incr_list(test_case2)
assert result_case2 == [6, 4, 6, 3, 4, 4]

# Test case 3: empty list
test_case3 = []
result_case3 = incr_list(test_case3)
assert result_case3 == []

# Test case 4: list with one element
test_case4 = [9]
result_case4 = incr_list(test_case4)
assert result_case4 == [10]

# Test case 5: complex tuple
test_case5 = (9, 8)
result_case5 = incr_list(test_case5)
assert result_case5 == [(10, 9), (11, 10)]
```
The function `incr_list` takes a list `l` as input and returns a new list with elements incremented by 1. The test cases are designed to check if the `incr_list` function works correctly for different types of input lists.