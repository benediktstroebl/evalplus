

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    a = float(a)
    h = float(h)
    return f"{a * h / 2:.3f}"
