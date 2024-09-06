```python
def max_element(l: list):
    """Return maximum element in the list
    >>> l = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    >>> max_element(l)
    123
    """
    return max(l)

# Test the function with the same input and output
def test_max_element():
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```