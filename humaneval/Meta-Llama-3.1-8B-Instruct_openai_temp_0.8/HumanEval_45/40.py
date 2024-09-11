```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    The area of a triangle is calculated using the formula: area = (base * height) / 2
    
    Args:
    a (float): The base length of the triangle.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Example usage
print(triangle_area(5, 3))
```

This script defines a `triangle_area` function that takes the base length `a` and the height `h` of a triangle as input, and returns the area of the triangle. The example usage at the end shows how to use the function to calculate the area of a triangle with base length 5 and height 3.