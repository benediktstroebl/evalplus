```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with various lists
assertEqual(max_element([1, 2, 3]), 3)
assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)
assertEqual(max_element([-5, -3, -10]) , -10)
```
The code defines a Python function max_element that takes a single argument l, which is expected to be a list. The function returns the maximum element in the list using the built-in max() function. The code then provides three test cases for the function, each one checking that the returned maximum matches the expected result using the assert statement.