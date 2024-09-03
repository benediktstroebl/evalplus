def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    a, b, c = a, b, c - h
    return ((a - b) * (c - b) + (a - c) * (b - c))

