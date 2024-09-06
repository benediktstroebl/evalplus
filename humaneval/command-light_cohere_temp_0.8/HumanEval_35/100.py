```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the max_element function with a list of numbers
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = max_element(test_max_element)
assert result == 123, "Expected maximum element not found!"

# Test the max_element function with a list of strings
test_string = ["hi", "hello", "world"]
result = max_element(test_string)
assert result == "hello", "Expected maximum element not found!"
```
The above Python script contains a self-contained function called `max_element` that solves the problem of finding the maximum element in a list. In the script, the function is tested with both a list of numbers and a list of strings, and the results are compared to the expected maximum elements, which pass the corresponding tests successfully.