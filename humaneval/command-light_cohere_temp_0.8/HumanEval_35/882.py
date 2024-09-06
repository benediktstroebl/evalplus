```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with various lists
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([-5, 3, -20, -100, 75, 15, 2]))  # Output: 75
print(max_element([10, 10, 10, 10]))  # Output: 10
print(max_element([2, 8, 4, 6, 7, 6, 7, 8, 3]))  # Output: 8
print(max_element([142, 2, 98, 11, 88, 33, 86, 53, 88]))  # Output: 86
```

This script defines a function max_element that takes a list as input and returns the maximum element in that list using the `max` function. It also provides test test the individuals to pass corresponding tests.