```python
def triangle_area(a, h):
    """Return the area of a triangle given a side length and height.
    Works for scalene triangles too.
    
    Args:
    - a (float): Length of side of the triangle
    - h (float): Height of the triangle
    
    Returns:
    - float: Area of the triangle a^(1/2) * h
    """
    return pow(a, 0.5) * h
```