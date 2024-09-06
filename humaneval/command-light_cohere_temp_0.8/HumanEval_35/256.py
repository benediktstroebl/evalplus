```python
def max_element(lst):
    return max(lst)

# Test case 1
test_case1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
if max_element(test_case1) != 123:
    raise Exception("Function did not return the correct maximum element!")

# Test case 2
test_case2 = [-5, 3, -10]
if max_element(test_case2) != -10:
    raise Exception("Function did not return the correct maximum element!")

# Test case 3
test_case3 = [1, 2, -3]
if max_element(test_case3) != -3:
    raise Exception("Function did not return the correct maximum element!")
```
The provided code defines a function max_element that calculates and returns the maximum element from a given list. This function is a output. The code then includes a test cases, and ensures the function is working correctly by comparing its output with expected maximum values.