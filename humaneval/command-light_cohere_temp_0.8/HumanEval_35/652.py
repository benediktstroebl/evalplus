```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test case 1:
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_max_element) == 123

# Test case 2:
test_max_element = [1, 2, 3]
assert max_element(test_max_element) == 3

# Test case 3:
test_max_element = [-5, -3, 3, 2, -10]
assert max_element(test_max_element) == 3

# Test case 4:
test_max_element = [1, 2, 3, 4, 5]
assert max_element(test_max_element) == 5

# Test case 5:
test_max_element = [10, 10, 10]
assert max_element(test_max_element) == 10

```
The above Python code defines a `max_element` function that takes a list as an argument and returns the maximum element in the list using the `max()` function. The code also includes several test cases to verify the correctness of the `max_element` function.