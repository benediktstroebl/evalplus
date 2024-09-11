```python
# Function to calculate the area of a triangle
def triangle_area(a, h):
    """
    Given length of a side (base) and height return area for a triangle.
    
    Parameters:
    a (float): Base of the triangle
    h (float): Height of the triangle
    
    Returns:
    float: Area of the triangle
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive numbers.")
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that takes the base and height of a triangle as parameters and returns its area. It also includes a test case at the end to demonstrate the function's usage. If you pass in non-positive values for the base or height, it raises a `ValueError` because the area of a triangle is only defined for positive values of these parameters.