def triangle_area(a, h):
    """Return the area of a triangle given a side length and height.
    Uses Heron's formula.
    
    Args:
    - a (float): Length of side (e.g., 5 in triangle ABC).
    - h (float): Height (e.g., 3 for ABC).
    
    Returns:
    - float: Area of the triangle.
    """
    sqrt(a**2 + h**2) / 2
    return round(sqrt(a**2 + h**2) / 2, 2)