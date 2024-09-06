```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the lengths of its sides.
    Args:
        a (float): The length of the first side
        h (float): The length of the second side
    Returns:
        float: The area of the triangle
    """
    assert isinstance(a, (int, float)), "First side must be a number"
    assert isinstance(h, (int, float)), "Second side must be a number"
    assert a + h > 0, "Second side must be longer than first side"
    return 0.5 * (a / h)
```