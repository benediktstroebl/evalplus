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
        raise ValueError("Height and side lengths must be positive")
    
    area = 0.5 * a * h
    return area
```

The function incorporates input validation to check that the input values are positive, raising a ValueError if they are not. To calculate the area of a triangle, the formula used is `0.5 * base * height`. This formula is used to compute the area and returned accordingly.

To test, ensure you run this function with different inputs, like `triangle_area(5, 3)` for a triangle with a base of 5 and a height of 3, and it should return 7.5 which is the correct area of the triangle.