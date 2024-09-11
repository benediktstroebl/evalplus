### Python Script to Calculate Triangle Area

```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    Args:
        a (float): The length of the base side of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base `a` and height `h`. The function uses the formula for the area of a triangle: `A = 0.5 * b * h`, where `b` is the base and `h` is the height. The function is then tested with a sample input.