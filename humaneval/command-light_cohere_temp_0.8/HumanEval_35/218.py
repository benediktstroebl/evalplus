```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test function to check if max element of list is calculated correctly
def test_max_element(lst):
    m = max_element(lst)
    assert m == max(lst), f"Wrong maximum element: {m} != {max(lst)}"

# Test list
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

# Test cases
test_max_element(test_list)
test_max_element([1, 2, 3])
test_max_element([-5, -3, -10, -20])
```
The function max_element takes a list as an argument and returns the maximum element in the list. The test_max_element function checks if the result of the max_element function is correct for different test lists.