```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test case 1
test_case_1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_case_1) == 123

# Test case 2
test_case_2 = [-5, 3, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_case_2) == 123

# Test case 3
test_case_3 = [5, 3, -5, 2, -3]
assert max_element(test_case_3) == 3
```