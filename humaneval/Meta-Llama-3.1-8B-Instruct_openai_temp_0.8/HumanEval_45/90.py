```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    The formula used to calculate the area of a triangle is:
    area = (base * height) / 2
    
    Parameters:
    a (float): The base of the triangle
    h (float): The height of the triangle
    
    Returns:
    float: The area of the triangle
    
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base and height. It uses the formula `area = (base * height) / 2` to calculate the area. The script also includes a docstring to provide documentation for the function and a test case to verify that the function is working correctly.