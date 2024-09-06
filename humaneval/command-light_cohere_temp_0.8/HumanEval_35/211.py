```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with various inputs
test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
test_max_element([])
test_max_element([1, 2, 3])
test_max_element([10, 1, 2])
test_max_element([5, -5, -10, -3])
test_max_element([0, 0, 0])
```
The function max_element returns the maximum element in the list. It utilizes the max function from the Python to find the maximum element in the list. The test cases validate the