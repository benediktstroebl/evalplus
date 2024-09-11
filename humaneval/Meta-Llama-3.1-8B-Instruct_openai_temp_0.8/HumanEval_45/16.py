```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.
    
    Parameters:
    a (float): The length of a side of the triangle.
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

This script defines a function `triangle_area` that calculates the area of a triangle given the length of a side (a) and the height (h). The area is calculated using the formula 0.5 * a * h. The function includes a docstring that explains its parameters, return value, and provides an example usage. The script also includes a test case to demonstrate how to use the function.