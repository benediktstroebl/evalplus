```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    Parameters:
    a (float): Length of the side.
    h (float): Height of the triangle.
    
    Returns:
    float: Area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that takes two parameters `a` (length of the side) and `h` (height of the triangle) and returns the area of the triangle. The area is calculated using the formula `0.5 * a * h`. The script then tests this function with the example provided.