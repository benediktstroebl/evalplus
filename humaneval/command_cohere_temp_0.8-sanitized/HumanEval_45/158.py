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
    # According to the sine formula, the area is `abs(a * h)` or `0.5 * a * h` depending on the triangle
    return 0.5 * abs(a) * h