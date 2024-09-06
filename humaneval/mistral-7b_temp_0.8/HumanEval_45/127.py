

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    if not (a>0 and h>0):
        return None
    area = 0.5*a*h
    return area
