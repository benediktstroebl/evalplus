```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    Parameters:
    a (float): Length of a side.
    h (float): Height of the triangle.
    
    Returns:
    float: Area of the triangle.
    
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base length `a` and height `h`. The formula used is `Area = 0.5 * base * height`. The function includes a docstring that provides documentation and an example usage. The script also includes an example usage at the end to demonstrate how to use the function.