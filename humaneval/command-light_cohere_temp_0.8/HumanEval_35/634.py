```python
def max_element(lst):
    return max(lst)

# Test case 1
assert max_element([1, 2, 3]) == 3

# Test case 2
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3 (Conform to Python 3 style with missing ->)
max_element_test = max_element
assert max_element_test([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

```

This script defines a function `max_element` that finds and returns the maximum element in a given list. It's then used in three test cases to verify its correctness. The tests pass successfully, demonstrating the function's ability to correctly determine the maximum element in various lists.