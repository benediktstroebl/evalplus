```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    The area of a triangle can be calculated using the formula:
    A = 0.5 * base * height
    
    Parameters:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    area = 0.5 * a * h
    return area

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base `a` and height `h`. The formula used for the calculation is `A = 0.5 * base * height`. The script includes a docstring to provide documentation and an example usage of the function.