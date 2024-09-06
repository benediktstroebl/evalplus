```python
def triangle_area(a, h):
    """Calculate the area of the triangle.
    Parameters:
    a: float or None, length of the first side
    h: float or None, length of the second side
    Returns: float, area of the triangle
    """
    assert a is not None and h is not None, "Both sides cannot be None"
    assert type(a) == float and type(h) == float, "Both sides must be float"
    return 0.5 * (a + h) ** / 2
```