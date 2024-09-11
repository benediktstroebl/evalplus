```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height return area for a triangle.
    
    The formula used for the area of a triangle is (base * height) / 2.
    
    Parameters:
    a (float): The base of the triangle.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base and height. It includes a docstring that provides a description of the function, its parameters, and its return value. The script also includes an example usage of the function and a test call to demonstrate its output.