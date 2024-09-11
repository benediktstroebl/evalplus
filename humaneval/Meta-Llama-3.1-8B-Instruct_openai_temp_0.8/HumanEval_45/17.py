```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    
    The area of a triangle can be calculated using the formula: 
    Area = (base * height) / 2
    
    Parameters:
    a (float): Length of a side
    h (float): Height of the triangle
    
    Returns:
    float: Area of the triangle
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both side and height must be positive")
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that takes two parameters: `a` (the length of a side) and `h` (the height of the triangle). The function uses the formula for the area of a triangle and returns the calculated area. It also includes a docstring to provide documentation for the function. The script includes a test at the end to demonstrate how to use the function.