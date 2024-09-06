```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

#Test case 1
test_incr_list = [1, 2, 3]
test_incr_list_result = incr_list(test_incr_list)
assert test_incr_list_result == [2, 3, 4]

#Test case 2
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_incr_list_result = incr_list(test_incr_list)
assert test_incr_list_result == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This code defines a function `incr_list` that adds 1 to each element of the input list, creating a new list. The test cases demonstrate the addition and assertion of the function. The code follows the test_casibility guidelines and provides clear and concise code with the function and tests.