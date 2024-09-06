```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with some sample inputs
# assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
# This will pass

# This will fail (element with the maximum value is 123, but the function returns 123)
[-5, 5, 3, 2, -3, -10]
```