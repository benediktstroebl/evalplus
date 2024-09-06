```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with various input lists
for _ in range(10):
    l = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(l) == max([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```