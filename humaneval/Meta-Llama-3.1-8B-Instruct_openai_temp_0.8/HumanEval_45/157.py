```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    The formula for the area of a triangle is: 
    area = (base * height) / 2
    
    Parameters:
    a (float): The length of the side (also considered as the base).
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Testing the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base (`a`) and height (`h`). The formula used is `area = (base * height) / 2`. The function includes a docstring with information about its parameters, return value, and an example usage. The script also includes a test call to the function to demonstrate its usage.