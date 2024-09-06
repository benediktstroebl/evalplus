

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    if a == 0 or h == 0:
        return 0
    else:
        return a * (h/2) ** 2
