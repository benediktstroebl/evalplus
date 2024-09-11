```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    
    Args:
        a (float): The base of the triangle.
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

This script defines a function `triangle_area` that calculates the area of a triangle given its base and height. The base and height are passed as arguments to the function. The function uses the formula for the area of a triangle (0.5 * base * height) and returns the result. The script also includes a test of the function by calling it with the example values 5 and 3.