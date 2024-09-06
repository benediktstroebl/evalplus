```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test function
def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    max_element = max_element(test_list)
    assert max_element == 123
```