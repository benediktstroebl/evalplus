```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    The formula used is (base * height) / 2.
    
    Args:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive.")
    return (a * h) / 2

# Example usage:
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that calculates the area of a triangle given the base and height. It includes a docstring with details about the function's parameters, return value, and example usage. The function also includes a check to ensure that both the base and height are positive, and raises a `ValueError` if they are not.