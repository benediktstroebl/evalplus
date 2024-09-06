```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test case 1
assert max_element([1, 2, 3]) == 3

# Test case 2
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3
assert max_element([-5, -3, 3, -10, 0, double(-3), 10]) == -3

# Test case 4
try:
    assert max_element([-5, -3, 3, -10, 0, double(-3), 10, double(10), 10]) == 10
except AssertionError:
    assert False  # Replace with your testing library's desired error message here

# Test case 5
try:
    assert max_element([1, 2, 3, 4, 5]) == 5
except AssertionError:
    assert False  # Add your error handling code here

```
This code provides a Python function `max_element` that takes a single argument `l`, which is a list. It then uses the manual maximum selection, or the `max` function from the Python standard library, to return the maximum element in the list.

The function is then tested using the `assert` statement, which verifies that the function returns the correct maximum element for a variety of input lists. The test cases cover a standard cases and edge cases and will fail if the function does not return the correct result. 

Please note that the function does not include any built-in testing libraries.