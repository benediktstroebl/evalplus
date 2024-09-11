```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    Args:
        a (float): Length of a side of the triangle.
        h (float): Height of the triangle.
    
    Returns:
        float: Area of the triangle.
    
    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Expected output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given the length of a side and the height. It uses the formula for the area of a triangle (0.5 * base * height), and includes a docstring with documentation and examples to explain how the function works.