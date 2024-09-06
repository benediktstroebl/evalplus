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
    
    return 0.5 * a * h
```

The function `triangle_area` calculates the area of a triangle given the length of a side `a` and its height `h` using the formula `0.5 * a * h`. The script also includes a test to check the functionality of the function. You can use the `triangle_area` function in your project to calculate the area of any triangle as long as you provide a side length and a height.  If any of the input values are less than or equal to zero, the function raises a `ValueError` and avoids any negative areas or zero-division issues.