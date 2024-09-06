```python
def max_element(lst):
    return max(lst)

# Test case 1
test_case1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_case1) == 123

# Test case 2
test_case2 = [5, 5, -5, -20, -40, -60]
assert max_element(test_case2) == -60

# Test case 3
test_case3 = [-5, 5, -10, -20, -15]
assert max_element(test_case3) == -15
```
This script defines a function max_element that returns the maximum element in a list, it takes a list as input and applies the maximum function to it, then returns the result. It also has three test cases, that verify the correctness of the max_element function.