```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test function to check if max_element function works correctly
def test_max_element(lst):
    result = max_element(lst)
    print(result)
```
The function `max_element` takes a list `lst` as input and returns the maximum element in the list. It uses the maximum function to get the maximum element from the list. The function is then tested by the `test_max_element` function, which creates a list `lst` and passes it to the `max_element` function to test its functionality.