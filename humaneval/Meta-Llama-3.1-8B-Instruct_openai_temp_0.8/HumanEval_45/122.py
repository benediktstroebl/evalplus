```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) of a triangle, return the area.
    
    Parameters:
    a (float): The length of a side of the triangle.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    Examples:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Example usage:
print(triangle_area(5, 3))
```

This script defines a function `triangle_area(a, h)` that calculates the area of a triangle given the length of a side `a` and the height `h`. The area is calculated using the formula `0.5 * base * height`, which is a standard formula for the area of a triangle. The function includes a docstring that describes its parameters, return value, and provides an example usage. The example usage at the end of the script demonstrates how to call the `triangle_area` function with specific values.