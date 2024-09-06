```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    Args:
        a (float): The length of a side of the triangle.
        h (float): The height of the triangle.
    Returns:
        float: The area of the triangle. 
    """
    triangle_height = (a / 2) * h
    area = 0.5 * triangle_height * a
    return area
```