```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with various lists
def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5]) == 3
    assert max_element([5, -5, 3, 2, 3, 9, 0, 123]) == 123
    assert max_element([-5, -3, 3, -10]) == -5
    assert max_element([-5, 3, 5, -10]) == -10
    assert max_element([1, 2, 3, 4, 5]) == 5
```