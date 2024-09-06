```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test the function with a sample list
test_max_element = max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert test_max_element == 123

# Another test with different list
test_result = max_element([1, 2, 3, -20])
assert test_result == -20
``` 
This Python code defines a function max_element that aims to return the maximum element in a given list. It achieves this by utilizing the max function to find the maximum element in the list. The code then follows up the testing this function with different sample lists and asserting the results.