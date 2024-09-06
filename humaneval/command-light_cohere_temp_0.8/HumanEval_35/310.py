```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with various inputs
def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5]) == 3
    assert max_element([5, -5, 3]) == 3
    assert max_element([-5, -3, 3, 5]) == 3
    assert max_element([0, 0, 1]) == 0
    assert max_element([123, 0, 1]) == 1
    assert max_element([-10, -3, -5, -20]) == -20
    assert max_element([]) == None
    assert max_element([1, 2, 3, 4, 5]) == 5  # Wrong input, expected max of individual elements
```