

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    if h <= 0:
        return 0
    else:
        return (h/2)**2 + (a/2)**2
