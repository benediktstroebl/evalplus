### Python Script: Calculate Triangle Area
```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.

    The formula used is: area = 0.5 * base * height

    Args:
        a (float): Length of a side.
        h (float): Height of the triangle.

    Returns:
        float: Area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both length of a side and height must be positive.")
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```
This Python script defines a function `triangle_area` that calculates the area of a triangle given its base and height. The function uses the formula `area = 0.5 * base * height`. It also includes input validation to ensure that both the base and height are positive numbers.