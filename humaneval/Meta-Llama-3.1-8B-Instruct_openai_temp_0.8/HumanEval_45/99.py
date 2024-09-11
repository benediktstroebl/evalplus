```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    Parameters:
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

This script defines a function `triangle_area(a, h)` that calculates the area of a triangle given the length of its base `a` and its height `h`. The area is calculated using the formula `A = 0.5 * b * h`, where `A` is the area, `b` is the base, and `h` is the height. The function is then tested with the example provided in the docstring.