```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    The formula for the area of a triangle is:
    area = 0.5 * base * height
    
    Parameters:
    a (float): Length of the base of the triangle.
    h (float): Height of the triangle.
    
    Returns:
    float: Area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that takes the base `a` and height `h` of a triangle as input and returns its area. The area of a triangle is calculated using the formula `0.5 * base * height`. The script also includes a test case to demonstrate the function's usage.