```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with a list of numbers
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = max_element(test_max_element)
assert result == 123, "Max element should be 123"
```
The provided code defines a Python function `max_element` that aims to return the maximum element from the input list. The function uses the simple Python's `max()` function to achieve this. 

The test cases are set up to ensure that the function correctly identifies the maximum element in the given list.