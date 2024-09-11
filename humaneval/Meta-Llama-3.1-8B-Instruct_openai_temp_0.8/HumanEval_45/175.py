```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.

    Args:
        a (float): The length of the side of the triangle.
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
print(triangle_area(4, 6))
print(triangle_area(10, 2))
```

This script defines a function `triangle_area` that calculates the area of a triangle given the length of a side and the height. The function uses the formula for the area of a triangle, which is `0.5 * base * height`. The script also includes several test cases to demonstrate the function's usage.