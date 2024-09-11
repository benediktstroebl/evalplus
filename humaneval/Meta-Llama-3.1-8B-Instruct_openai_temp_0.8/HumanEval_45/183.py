```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height return area for a triangle.

    Args:
    a (float): Length of the side (base of the triangle).
    h (float): Height of the triangle.

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

This script defines a function `triangle_area` that calculates the area of a triangle given its base and height. It uses the formula for the area of a triangle, which is `0.5 * base * height`. The script then tests this function with the example provided and prints the result.