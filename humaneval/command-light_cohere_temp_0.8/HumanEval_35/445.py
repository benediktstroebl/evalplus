```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test function
def test():
    l = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(l) == 123

# Run the function and test it
test()
```