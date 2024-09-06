def triangle_area(a, h):
    """
    Calculates the area of a triangle given the length of a side and its height.
    Args:
        a (float): The length of a side of the triangle.
        h (float): The height of the triangle.
    Returns:
        float: The area of the triangle.
    """
    # Based on the Pythagorean theorem, the formula for the area of a triangle
    # with sides a and h is sqrt(a * a + h * h) / 2.
    area = (math.sqrt(a * a + h * h) / 2)
    return area