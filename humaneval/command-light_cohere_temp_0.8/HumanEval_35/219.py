```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with different inputs
assertEqual(max_element([1, 2, 3]), 3)
assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) , 123)
assertEqual(max_element([4, 12, e))), 12)
```
The code defines a function `max_element` that takes a list as input and returns the maximum element in the list. The `test_max_element` test function verifies that the `max_element` function returns the correct maximum element for different input lists. 

The `assertEqual` function is used for assertions and will print a failure message if the assertions are not true.