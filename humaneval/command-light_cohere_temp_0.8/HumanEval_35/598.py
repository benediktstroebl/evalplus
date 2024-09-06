```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with a list of numbers
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_max_element) == 123

# Test the function with a list of strings
test_str_element = ["5", "3", "-5", "2", ",-3", "3", "9", "0", "123", "1", "-10"]
assert max_element(test_str_element) == "123"
```
This script defines a function `max_element` that calculates and returns the maximum element from a given list. The test cases demonstrate the same approach using a list of numbers and strings, passing them to the `max_element` function.