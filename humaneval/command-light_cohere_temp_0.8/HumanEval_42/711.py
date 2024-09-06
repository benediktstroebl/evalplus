```python
def incr_list(lst):
    lst[:] = [lst[-1] + 1]
    return lst

# Test case 1
test_incr_list = [1, 2, 3]
test_incr_list_res = incr_list(test_incr_list)
assert test_incr_list_res == [2, 3, 4]

# Test case 2
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_incr_list_res = incr_list(test_incr_list)
assert test_incr_list_res == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3 (Edge case)
test_incr_list = [5, 2]
test_incr_list_res = incr_list(test_incr_list)
assert test_incr_list_res == [6]
```
The Python function `incr_list` takes a list `lst` as input and then increments the last element of the list by 1 and returns the modified list.  It also provides several test cases to ensure the correctness of the function.