```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with different lists
# First test with a list with both positive and negative numbers
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_max_element) == 123

# Second test with a list of strings
test_strings = ["hello", "world", "!!!!!"]
assert max_element(test_strings) == "!"

# Third test with a list of custom objects
class CustomObject:
    def __init__(self, x):
        self.x = x
    object = x
# Test with a list of objects with a custom method
        test_objects = [CustomObject(100), CustomObject(200), CustomObject(123)]
        assert max_element(test_objects) == 200
```