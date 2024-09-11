```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    The area of a triangle is calculated using the formula: area = (base * height) / 2
    
    Args:
    a (float): The length of the side (base).
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Example usage:
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base and height. The formula for the area of a triangle is `area = (base * height) / 2`, which is implemented in the function. The example usage at the end shows how to use the function with the given example values.