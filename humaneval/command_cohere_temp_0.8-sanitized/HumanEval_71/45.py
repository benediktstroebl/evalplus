def triangle_area(a, b, c):
    """
    Calculates the area of a triangle given its side lengths a, b, and c.
    Returns rounded area if valid, and -1 otherwise.
    
    Examples:
    >>> triangle_area(3, 4, 5)
    6.00
    >>> triangle_area(1, 2, 10)
    -1
    """
    s = sum([a, b, c])
    if len(set(s)) == 2 or (s[0] + s[1]) > s[2] and (s[0] + s[2]) > s[1] and (s[1] + s[2]) > s[0]:
        ar = (a * b * (s[0] * s[1] * s[2]) / (4 * sqrt(3)))
        return round(ar, 2)
    else:
        return -1