```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test function to pass the test
def test():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```

The provided function `max_element` in this code takes a list `lst` as input and returns the maximum element from the list using the `max()` built-in function. The test function is a simple case where we pass a list with integers and a string, respectively, and it should correctly return the integer.

The code is well-structured, follows good practices, and effectively solves the problem. You can use this template and design to create your own functions with ease.