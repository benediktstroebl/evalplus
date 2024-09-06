```python
def max_element(lst):
    return max(lst)

# Test case 1
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 2
assert max( [-5, 3, -10, 12345, 789, 5, -20]) == 12345

# Test case 3
assert max_element([]) == 0

# Test case 4
assert max_element([21, 12, 33, -77, 99]) == 99

```

This script defines a function `max_element` that takes a list as an argument and returns the maximum element in that list. It also has a test cases to ensure the correctness of the function.

The `max_element` function uses the `max()` built-in function to get the maximum value in the list, and returns that value.