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
    b = a ** 2 + h ** 2  # Pythagorean theorem
    # Calculate area using formula
    area = 0.5 * a * b
    return area