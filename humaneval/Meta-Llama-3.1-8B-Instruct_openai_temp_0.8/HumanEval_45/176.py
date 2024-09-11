### Calculating Triangle Area
```python
def triangle_area(a, h):
    """
    Given length of a side (base) and high (height) return area for a triangle.
    
    The area of a triangle is calculated using the formula:
    area = 0.5 * base * height
    
    Args:
        a (float): Length of the base of the triangle.
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
This Python script defines a function `triangle_area` that calculates the area of a triangle given its base and height. It then tests this function with a sample calculation. The function is well-documented with a docstring that explains its purpose, parameters, return value, and provides an example usage.