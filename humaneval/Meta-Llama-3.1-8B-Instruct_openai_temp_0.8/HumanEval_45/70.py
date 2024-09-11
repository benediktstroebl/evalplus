```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height return area for a triangle.
    
    Parameters:
    a (float): Base of the triangle.
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

This script defines a function `triangle_area` that calculates the area of a triangle given its base and height. The function uses the formula for the area of a triangle: `A = 0.5bh`, where `b` is the base and `h` is the height. The script then tests this function with the example given in the problem statement.