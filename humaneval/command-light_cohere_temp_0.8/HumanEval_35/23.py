```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the max_element function
lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(lst) == 9

# Test with list of strings
lst = ["Hello", "World"]
assert max_element(lst) == "World"

# Test with empty list
assert max_element([]) == None
```
This script provides a function `max_element` that takes a list as input and returns the maximum element in the list using the `max()` built-in function. The test cases ensure that the function works correctly with various lists and empty lists.