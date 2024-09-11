```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    The formula used to calculate the area of a triangle is: area = (base * height) / 2
    
    Parameters:
    a (float): Length of a side (base) of the triangle.
    h (float): Height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    Examples:
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area(a, h)` that calculates the area of a triangle given the length of a side (base) `a` and the height `h`. The area is calculated using the formula `area = (base * height) / 2`. The function includes a docstring that describes its parameters, return value, and provides an example usage. The script also includes a test call to the function with the example values.