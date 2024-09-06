def triangle_area(a, h):
    """Return the area of a triangle given a side length and height.
    
    Args:
    - a (float): Side length of triangle
    - h (float): Height of triangle
    
    Returns:
    - float: Area of triangle aycient
    
    Reference:
    https://www.mathsisfun.com/geometry/triangle-area- formulas.html
    """

    # Prefix property
    # (Also known as Heron's Formula)
    # https://www.mathsisfun.com/geometry/trig-precentages.html
    # sqrt((a^2 + b^2 + c^2)/2) = hypotenuse
    hypotenuse = math.sqrt((a**2 + h**2 + (a**2 - h**2)**2) / 2)
    area = 0.5 * a * h * hypotenuse
    return area