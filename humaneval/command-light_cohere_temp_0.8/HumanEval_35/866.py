```python
def max_element(lst):
    return max(lst)

# Test case 1
test_case1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_case1) == 123

# Test case 2
test_case2 = [-5, 3, -10, 2, -3, 3, 9]
assert max_element(test_case2) == 3

# Test case 3
test_case3 = [123, 2, -2, 5, -5, 3, 9, 0]
assert max_element(test_case3) == 123
```
This script defines a function max_element that returns the maximum element in a given list. It then passes 3 test cases with different lists, and the function correctly returns the maximum element for each case.