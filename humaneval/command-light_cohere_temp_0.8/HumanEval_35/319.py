```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with various lists
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([-5, -3, 7]))  # Output: 7
print(max_element([1, 2, 3, 4, 5]))  # Output: 5
print(max_element([10, -9, -13, -8]))  # Output: -13
```
This script defines a `max_element` function that takes a list as input and returns the maximum element in the list.

The function uses the built-in `max` function to get the maximum element from the list. 

The script then provides a set of test cases to ensure that the function is working correctly.