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
    if h == 0: 
        return 0  # Return 0 if height is 0 to avoid division by zero
    s = (a * h) / 2  # Base times height divided by 2
    area = s * (2 * math.sqrt(3) / 3)  # Area formula: sqrt(s * (s-a) * (s-a))
    return area