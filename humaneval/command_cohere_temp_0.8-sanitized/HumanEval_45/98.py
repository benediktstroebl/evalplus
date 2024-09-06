def triangle_area(a, h):
    """Return the area of a triangle given a side length and height.
    Uses Heron's formula."""
    s = (a**2 + h**2) / 2
    area = sqrt(s * (s - a**2) * (s - h**2)) / 2
    return area