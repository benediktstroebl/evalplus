

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    if h < 0:
        return "High must be greater than or equal to 0"
    return 0.5 * a * h

