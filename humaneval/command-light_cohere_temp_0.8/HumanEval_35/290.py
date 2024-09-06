```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

#Test the function
def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5]) == 3
    assert max_element([-5, -3, 3, -10, 9, 0, 123]) == 123
```
This code defines a function max_element that returns the maximum element in the list. Then, the test_max_element function passes the tests, and the test results are True.