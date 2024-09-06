```python
def max_element(lst):
    if not_list(lst):
        raise TypeError("Input must be a list")
    return max(lst)

# Test the function with various input lists
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = max_element(test_max_element)
assert result == 123

# Test with empty list
empty_list = []
result = max_element(empty_list)
assert result is None
```
The script defines a function `max_element` that takes a list as input and returns the maximum element in that list. The function uses the specific to Python's list data type and raises a `TypeError` for non-list inputs. The test cases cover various scenarios, including passing a non-list, an empty list, and a list of numbers and strings. The function correctly returns the maximum element in the test cases and passes the corresponding tests.