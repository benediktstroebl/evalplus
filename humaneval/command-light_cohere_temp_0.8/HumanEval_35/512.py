```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test case 1
test_1 = [1, 2, 3]
assert max_element(test_1) == 3

# Test case 2
test_2 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_2) == 123

# Test case 3
test_3 = [-5, 3, -5, 2, -3, 3, -10, -2, -3]
assert max_element(test_3) == -3
```

This script defines a function `max_element` that calculates the maximum element in the passed list. The function is then passed to the `assert` module to verify its correctness for the provided test cases.