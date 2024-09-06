```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with various list inputs
assert(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == 123
assert(max_element([-5, -3, -10])) == -5
assert(max_element([1, 2, 3, 4, 5])) == 5
assert(max_element([44, 11, 22, 13, 66])) == 66
```
This script defines a function `max_element` that calculates and returns the maximum element in the provided list. 

The test section ensures the function is correctly applied to various types of lists.