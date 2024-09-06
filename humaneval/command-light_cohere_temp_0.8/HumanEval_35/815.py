```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with a list of various types
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(test_max_element))  # Output: 123

# Test the function with a list of strings
test_string_element = ["help", "test", "me"]
print(max_element(test_string_element))  # Output: None

# Test the function with a list containing only one element
test_single_element = [42]
print(max_element(test_single_element))  # Output: 42
```
The script defines a function max_element that takes a list as input and returns the maximum element in the list. It then provides several tests to validate the correctness of this function.