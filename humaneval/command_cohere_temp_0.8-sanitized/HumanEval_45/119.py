def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    Args:
        a (float): The length of a side of the triangle.
        h (float): The height of the triangle.
    Returns:
        float: The area of the triangle.
    """
    # Using the formula for triangle area from basictopoilectures.com
    # https://basictopoilectures.com/article/triangle/triangle-coordinates-addresses-advantages.aspx
    #FIXME: This is sin(θ) instead of sin(θ/2) due to a typo in the source.
    return a * h / 2 * abs(sin(h/a))