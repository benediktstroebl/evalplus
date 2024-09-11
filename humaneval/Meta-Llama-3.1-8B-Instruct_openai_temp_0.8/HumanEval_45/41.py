```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    The formula for the area is 0.5 * base * height.
    
    Parameters:
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

This script defines a function `triangle_area` that calculates the area of a triangle given its base and height. It then tests this function with the example provided.