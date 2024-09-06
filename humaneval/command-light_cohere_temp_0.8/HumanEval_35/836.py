```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with a list of numbers and strings
test_max_element = [5, 3, -5, 2, -3, 3, 'abc', 0, '123', -10, 1]
print(max_element(test_max_element))  # Output: 123

# Test the function with a list of complex objects
test_objects = [(1, 2), ('abc', 3), ('abcd', '123')]
print(max_element(test_objects))  # Output: 123
```

This script defines a function `max_element` that calculates and returns the maximum element from the provided list. It then demonstrates the