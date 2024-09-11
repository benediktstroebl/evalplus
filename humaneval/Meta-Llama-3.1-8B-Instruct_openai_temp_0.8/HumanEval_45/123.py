```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    
    The formula used is area = 0.5 * base * height.
    
    Args:
        a (float): Length of the side.
        h (float): Height of the triangle.
    
    Returns:
        float: Area of the triangle.
    
    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))
```

This script defines the `triangle_area` function, which calculates the area of a triangle given the length of a side `a` and the height `h`. The function uses the formula `area = 0.5 * base * height` and returns the calculated area. The script also includes a test case to verify the function's correctness.