```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

#Test the function
def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5]) == 3
    assert max_element([-5, -3, -10]) == -5
    assert max_element([5, 0, 123]) == 123
    assert max_element([]) == 0
```
This script defines a function max_element that finds the maximum element in a list. It is then test this function with a series of inputs and asserts to ensure its correctness.