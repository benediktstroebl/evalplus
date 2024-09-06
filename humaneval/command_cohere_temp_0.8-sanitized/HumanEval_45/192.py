def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    Args:
        a (float): The length of a side of the triangle.
        h (float): The height of the triangle.
    Returns:
        float: The area of the triangle. 
    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    triangle_area = (a * h) / 2  # Triangle area formula
    return triangle_area