

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    assert h < a and a < 1.5 * h
    return 0.5 * h * (a + h)
