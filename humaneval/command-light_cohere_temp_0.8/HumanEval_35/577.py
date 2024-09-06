```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test with empty list
assert max_element([]) == None

# Test with list of strings
assert max_element([["a", "b", "c"]) == "c"
``` 
This script defines a function max_element that finds the maximum element in a given list. It uses the approach of `max()` to find the largest element. The test cases validate that the function is correct and will throw an `AssertionError` if the result doesn't match the expected output.