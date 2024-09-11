```python
def triangle_area(a, h):
    """
    Given length of a side 'a' and height 'h', return the area for a triangle.
    
    Parameters:
    a (float): length of a side of the triangle
    h (float): height of the triangle
    
    Returns:
    float: the area of the triangle
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given the length of a side and the height. It uses the formula for the area of a triangle: `A = 0.5 * base * height`. The script includes a docstring to provide documentation for the function, and it includes an example usage to demonstrate how to call the function.