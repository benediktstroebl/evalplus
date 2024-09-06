```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(l[-1] + 1)
    return l

# Test case 1
test_case1 = [[1, 2, 3]]
test_case1_res = incr_list(test_case1)
print("Test case 1 result:", endswith(test_case1_res))

# Test case 2
test_case2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_case2_res = incr_list(test_case2)
print("Test case 2 result:", endswith(test_case2_res))

# Test case 3
test_case3 = [1, 2, 3, 4, 5, 6, 7]
test_case3_res = incr_list(test_case3)
print("Test case 3 result:", endswith(test_case3_res))
```
The function `incr_list` takes a list `l` as an argument. It appends one to the list and returns the modified list.

The test cases follow the same pattern, where you pass a list of numbers and then call the `incr_list` function to get the result.

We've added some test cases to demonstrate the functionality of the `incr_list` function.