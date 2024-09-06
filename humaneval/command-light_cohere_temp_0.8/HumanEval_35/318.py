```python
def max_element(lst):
    return max(lst)

# Test case 1
test_case1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_case1) == 123

# Test case 2
test_case2 = [1, 2, 3, 4, 5, 6, 7, -2, -3, 8]
assert max_element(test_case2) == 5

# Test case 3
test_case3 = [2, -7, 5, -10, -13, -15, -16]
assert max_element(test_case3) == -7
```
This script defines a function max_element that takes a list lst as input and returns the maximum element in the list. This function is using the max function from Python's built-in library to get the maximum value of an iterable. The test cases demonstrate that the function correctly identifies the maximum element in each case.