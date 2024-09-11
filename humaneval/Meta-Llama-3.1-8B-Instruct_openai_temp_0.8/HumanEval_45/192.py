```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    Args:
        a (float): The length of a side of the triangle.
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

This script defines a function `triangle_area` that calculates the area of a triangle given the length of a side and the height. The function uses the formula for the area of a triangle, A = 0.5 * b * h, where b is the base and h is the height. The script also includes a test to demonstrate the function's usage.