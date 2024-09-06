```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function
assert(max_element([1, 2, 3]) == 3)
assert(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123)
```
This code defines a max_element function that takes an input list and returns the maximum element in that list. The test code at the example then verifies the correct behavior of the max_element function with various input lists.