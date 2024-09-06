```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1
test_case1 = [1, 2, 3]
test_result1 = incr_list(test_case1)
assert test_result1 == [2, 3, 4]

# Test case 2
test_case2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result2 = incr_list(test_case2)
assert test_result2 == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3 (Should raise TypeError)
test_case3 = ['a', 2]
with pytest.assert expected_exception=TypeError():
    incr_list(test_case3)
```  The function incr_list takes a list l as input and returns a new list with the elements from input list incremented by 1. The test cases demonstrate the necessary functionality and also catch and assert the expected exceptions.