```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height return area for a triangle.

    Args:
        a (float): Length of the base (side) of the triangle.
        h (float): Height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Expected output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given the base `a` and height `h`. The function uses the formula for the area of a triangle, `A = 0.5 * b * h`, where `b` is the base and `h` is the height. The script then tests the function with the example provided.