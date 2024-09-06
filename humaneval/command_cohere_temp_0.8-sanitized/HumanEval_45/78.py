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
    # Calculate base of the triangle
    b = a / 2
    # Calculate area using Heron's formula
    area = 0.5 * h * b * math.sqrt(b**2 + h**2)
    return area