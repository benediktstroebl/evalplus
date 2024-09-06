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
    # Calculate area using Heron's formula
    area = 0.5 * (a * b * (h - b)**2) ** (1/3)
    return area
```