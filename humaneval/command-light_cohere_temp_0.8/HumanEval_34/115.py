```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return list(set(l))

# Test case 1
test_case_1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result_1 = unique(test_case_1)
assert test_result_1 == [0, 2, 3, 5, 9, 123]

# Test case 2
test_case_2 = [1, 2, 3, 4, 5, 6, 7]
test_result_2 = unique(test_case_2)
assert test_result_2 == [1, 2, 3, 4, 5, 6, 7]

# Test case 3
test_case_3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
test_result_3 = unique(test_case_3)
assert test_result_3 == [0, 1, 2, 3, 4, 5, 6, 7, 8]
``` 
This script defines a function `unique` that takes a list as an argument and returns a new list with unique elements. It then provides three test cases with lists and asserts that the `unique` function returns the expected output for each case.