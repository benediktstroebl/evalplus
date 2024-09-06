```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1
test_case1 = [1, 2, 3]
test_case1_result = incr_list(test_case1)
assert test_case1_result == [2, 3, 4]

# Test case 2
test_case2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_case2_result = incr_list(test_case2)
assert test_case2_result == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3 (with custom exception)
try:
    test_case3 = [10, 20, 30]
    incr_list(test_case3)
except TypeError as e:
    assert "list index out of range" in str(e)
    
# Test case 4 (empty list)
test_case4 = []
test_case4_result = incr_list(test_case4)
assert test_case4_result == []
```
The function `incr_list` in this script adds a number 1 to each element in the input list, producing a new list with the incremented values. The test cases demonstrate the essential that the function works as expected.