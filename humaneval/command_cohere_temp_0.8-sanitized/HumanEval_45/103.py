def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    base = a / 2  # Assuming the triangle is a right triangle (base)
    area = 0.5 * base * h
    return area