```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the max_element function with various lists
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_max_element) == 123

# Test with empty list
assert max_element([]) == None

# Test with list of strings
assert max_element(["hello", "world!"]) == "world!"
```
The code defines a function `max_element` that takes a list as input and returns the maximum element in that list. Additionally, it includes test cases for the function to ensure its correctness.