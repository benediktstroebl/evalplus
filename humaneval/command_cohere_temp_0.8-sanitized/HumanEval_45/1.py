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
    # Based on Heron's formula for triangle's area
    s = (a * h) / 2  # Calculating semi-perimeter
    area = sqrt(s * (s - a) * (s - h) * (s + h))  # Area of the triangle
    return area