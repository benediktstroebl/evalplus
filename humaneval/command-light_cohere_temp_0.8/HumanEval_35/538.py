```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the max_element function
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
# the output should be True

# Test the function with invalid input
assert max_element([1, 2, 3]) == 3
# the output should be False
``` 
This code provides a simple solution to the problem using the built-in Python function `max()`. The `max` function returns the maximum value of the list, which is then returned as the result of the `max_element` function.