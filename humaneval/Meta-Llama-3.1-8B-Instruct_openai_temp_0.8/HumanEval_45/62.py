```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.
    
    The formula used for the area of a triangle is 1/2 * base * height.
    In this case, the base is given by the length of the side (a).
    
    Args:
        a (float): The length of a side of the triangle.
        h (float): The height of the triangle.
    
    Returns:
        float: The area of the triangle.
    
    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that calculates the area of a triangle given its side length `a` and height `h`. The function uses the formula 1/2 * base * height for the area of a triangle, where the base is given by the length of the side `a`. The function is then tested with the example provided in the docstring.