```python
def incr_list(lst):
    n = len(lst)
    for i in range(n):
        lst[i] += 1
    return lst

# Test case 1: Test list comprehension
test_incr = [1, 2, 3]
expected = [2, 3, 4]
result = incr_list(test_incr)
assert result == expected, "Test case 1 failed."

# Test case 2: Test list assignment
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
result = incr_list(test_list)
assert result == expected, "Test case 2 failed."

# Test case 3: Test tuple assignment
test_tuple = (5, 3, 5, 2, 3, 3, 9, 0, 123)
expected = (6, 4, 6, 3, 4, 4, 10, 1, 124)
result = incr_list(test_tuple)
assert result == expected, "Test case 3 failed."
```
The provided Python script defines a function `incr_list` that incrementally every value in a given list by one. It offers three test cases to assess the effectiveness of this function: test case 1 and 2 utilize list comprehension to validate the updated list, while test case 3 validates the modified tuple.

This script effectively demonstrates how to use the `incr_list` function to update lists and validate the results using test cases.