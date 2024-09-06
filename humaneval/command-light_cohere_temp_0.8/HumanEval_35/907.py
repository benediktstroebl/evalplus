```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function
def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5]) == 3
    assert max_element([-5, -3, 3, 5, 7]) == 3
    assert max_element([]) == 0
    assert max_element([123, -10, 0]) == 0
```