```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with some examples
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```
This script defines a function `max_element` that takes a list `l` as input and returns the maximum element in the list. It achieves this by using the `max()` function, which returns the maximum value in the list. The `assert` statement is used to check if the function is working correctly by comparing its output with the expected result from the test case.