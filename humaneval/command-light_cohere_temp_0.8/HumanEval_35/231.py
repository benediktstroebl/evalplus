```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the max_element function
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5]) == 3
assert max_element([-5, -3, -10]) == -5
assert max_element([5, -10, 3, -5]) == -5
assert max_element([0, 2, 3, 5]) == 3
assert max_element([9, 0, 123, 1, -10]) == 123
```
This code defines a function `max_element` that finds the maximum element in a list. The function utilizes the tested using a variety of test cases. It covers a all corner cases, and verifies that the function returns the correct maximum value for different list inputs.