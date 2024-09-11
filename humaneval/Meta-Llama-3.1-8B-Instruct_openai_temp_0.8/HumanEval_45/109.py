```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height, return area for a triangle.
    
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

This script defines a function `triangle_area(a, h)` that calculates the area of a triangle given the base (`a`) and height (`h`). The formula used is `(base * height) / 2`. The script includes a test case to demonstrate its usage.