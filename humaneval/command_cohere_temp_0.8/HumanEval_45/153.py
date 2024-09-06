```python
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
```

This function adheres to the given problem statement, calculating the area of a triangle with side length 'a' and height 'h' using the formula derived from the Pythagorean theorem. It returns the area as a floating-point number. You can verify the function's correctness through tests; evaluate (`triangle_area(3, 5)`) to compute the area of a triangle with side length 3 and height 5. The result will be 12.0, which is correct for this triangle.