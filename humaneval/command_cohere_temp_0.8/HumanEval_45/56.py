```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    
    Args:
    - a (float): Length of a side of the triangle.
    - h (float): Height of the triangle.
    
    Returns:
    - float: Area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    if h <= 0 or a <= 0:
        raise ValueError("Height and length of side must be positive")
    
    area = 0.5 * a * h
    return area
```

The area of a triangle is calculated using the formula `0.5 * a * h` where `a` is the length of a side and `h` is the height or length of the triangle's legs opposite the angle between the sides of length `a` (or the triangle's base). This formula allows for calculating the triangle's area from any side and any height.

This code defines a function `triangle_area` that takes two arguments, `a` and `h`, and returns the area of the triangle. It includes a usage example and also performs some basic error checking to make sure that the input values are positive, raising a `ValueError` if they're not. 

To ensure the function remains robust, it's best practice to include additional test cases to cover a variety of scenarios, edge cases, and potential error conditions. These tests can be run against the function to validate its robustness.