

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("The value of a and h must be > 0.")
    return a * h / 2

