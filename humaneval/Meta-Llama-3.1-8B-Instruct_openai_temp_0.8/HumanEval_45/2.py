```python
def triangle_area(a, h):
    """
    Given length of a side (a) and high (h) return area for a triangle.
    
    The area of a triangle is calculated using the formula:
    area = 0.5 * base * height
    
    In this case, the base 'a' is assumed to be the side of the triangle.
    
    Parameters:
    a (float): The length of the side of the triangle.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base 'a' and height 'h'. It uses the formula `area = 0.5 * base * height` and returns the calculated area. The script includes a docstring that explains how to use the function, its parameters, and its return value. Finally, it tests the function with the example provided.