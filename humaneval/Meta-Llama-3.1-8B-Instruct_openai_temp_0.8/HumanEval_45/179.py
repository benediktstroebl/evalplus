```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    Parameters:
    a (float): Length of a side.
    h (float): Height of the triangle.
    
    Returns:
    float: Area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Side and height must be positive numbers.")
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that takes the length of a side and the height of a triangle as parameters, and returns their product divided by 2, which is the formula for the area of a triangle. The function also includes a check to ensure that the side and height are positive numbers. The example usage is shown at the end of the script.