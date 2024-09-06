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
        raise ValueError("Height and side length must be positive")
    
    area = 0.5 * a * h
    return area
```

The area of a triangle is calculated using the formula `0.5 * a * h` where `a` is the length of a side and `h` is the height or distance between the vertex opposite the side and the base of the triangle. This formula is encapsulated within the `triangle_area()` function, ensuring that positive values of `a` and `h` are required for valid inputs and returning the calculated area.

This function can be tested as demonstrated in the docstring with a side length of 5 and a height of 3, returning 7.5, confirming the correct operation of the function.