```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    Args:
        a (float): The side length of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that calculates the area of a triangle given its side length `a` and height `h`. The area is calculated using the formula `area = 0.5 * base * height`. The script also includes a docstring to provide documentation for the function and an example usage.