```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    Args:
        a (float): The base length of the triangle.
        h (float): The height of the triangle.
    
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

This script defines a function `triangle_area` that calculates the area of a triangle given its base length `a` and height `h`. The area of a triangle is calculated as half the product of its base and height. The script includes a docstring that explains the purpose of the function, its parameters, and its return value. The script also includes a test case at the end to demonstrate the function's use.