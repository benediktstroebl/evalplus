```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    
    Args:
    - a (float): Length of a side of the triangle.
    - h (float): Height of the triangle.
    
    Returns:
    - float: Area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    # Calculate base length
    b = a / (2 * sqrt(3))
    # Calculate area using formula
    area = 0.5 * a * h  # base * height
    # Adjust area for isosceles triangle
    area *= (1 / 2) ** 2
    return area
```