def triangle_area(a, h):
    """
    Calculates the area of a triangle given the length of a side and its height.
    Args:
        a (float): The length of a side of the triangle.
        h (float): The height of the triangle.
    Returns:
        float: The area of the triangle.
    """
    # Based on the Pythagorean theorem, the triangle's area is calculated as half of the square of the hypotenuse.
    return 0.5 * a * h