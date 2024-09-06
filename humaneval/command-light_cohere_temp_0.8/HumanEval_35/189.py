```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function
for _ in range(0):
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(test_list) == 123
```