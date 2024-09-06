```python
def triangle_area(a, h):
    """Calculate the area of the triangle.
    Input: a, h (side length and height respectively)
    Output: The area of the triangle
    """
    assert a > 0
    assert h > 0
    area = 0.5 * (a + h)
    return area
```