```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h), return the area for a triangle.
    
    The area of a triangle is calculated using the formula: 
    Area = (base * height) / 2
    
    Args:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    Examples:
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This Python script defines a function `triangle_area` that calculates the area of a triangle given its base `a` and height `h`. It uses the formula for the area of a triangle, which is `(base * height) / 2`. The function includes a docstring that explains its purpose, arguments, and return values, as well as an example usage.