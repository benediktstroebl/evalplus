```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst, key=lambda x: x)

# Test the function
def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123]) == 123
    assert max_element([]) == 0
    assert max_element([21, 12, 43, 7]) == 43
```