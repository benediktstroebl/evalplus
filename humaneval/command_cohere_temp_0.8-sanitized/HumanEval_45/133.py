def triangle_area(a, h):
    """Return the area of a triangle given the length of a side and its height.
    
    Args:
    - a (float): Length of a side of the triangle.
    - h (float): Height of the triangle.
    
    Returns:
    - float: Area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    # Calculate the area using the formula derived from the Heron's formula
    return 0.5 * a * h * (h - a ** min(2.0, 5)) / (2.0 * (h - a)**2)