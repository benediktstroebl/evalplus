

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return (a ** 2) / 4 - (h / 2) * (a ** 2) / 2
