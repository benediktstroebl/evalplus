```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test function
def test_max_element():
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(lst) == 123

# Test cases
test_max_element()
```

The above code defines a function `max_element` that returns the maximum element in the input list. The test function `test_max_element` contains a test list and asserts that the result of calling `max_element` with the test list is correct. The test cases will run the test_max_element() and pass the test.