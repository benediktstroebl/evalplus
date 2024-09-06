```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test case 1
test_case1 = [1, 2, 3]
print("Test case 1: ", max_element(test_case1))  # Output: 3

# Test case 2
test_case2 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print("Test case 2: ", max_element(test_case2))  # Output: 123

# Test case 3
test_case3 = [-5, 3, -3, 3, 9, 0, 123]
print("Test case 3: ", max_element(test_case3))  # Output: 123
```

The function `max_element` calculates the maximum element in the list. When you test with three test cases, it correctly returns `123` as the maximum element. 

Please note that this code is self-contained and does not require any external functions or modules. It demonstrates the simple and efficient solution for finding the maximum element in a list using Python's built-in `max()` function.