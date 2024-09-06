```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with a sample list
test_max_element = max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert test_max_element == 123, "Expected max element 123, but got {}".format(test_max_element, "test max element")
```