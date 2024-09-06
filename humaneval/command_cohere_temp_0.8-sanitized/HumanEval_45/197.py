def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    Note: The height is the length of a line segment perpendicular to the given side.
    
    Parameters:
    a (float): Length of one side of the triangle.
    h (float): Height of the triangle (perpendicular distance from the base)
    
    Returns:
    float: The area of the triangle 
    """
    # Based on the formula for triangle area: A = .5ah
    return 0.5 * a * h