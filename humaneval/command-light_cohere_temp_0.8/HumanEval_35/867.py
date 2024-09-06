```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function
def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5]) == 3
    assert max_element([-5, -3, -10, -20]) == -20
    assert max_element([-5, 3, -20]) == -20
    assert max_element([]) == float('-inf')
    assert max_element([1, 2, 3, 4, 5]) == 5
```