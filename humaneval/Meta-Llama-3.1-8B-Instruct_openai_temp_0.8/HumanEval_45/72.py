```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    Args:
        a (float): Length of a side of the triangle.
        h (float): Height of the triangle.
    
    Returns:
        float: The area of the triangle.
    
    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that calculates the area of a triangle given the length of a side and the height. The function uses the formula for the area of a triangle, which is `A = 0.5 * base * height`. It then tests the function with an example call to `triangle_area(5, 3)`.