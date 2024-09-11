```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.

    The formula used is: Area = (base * height) / 2

    Args:
        a (float): Length of the side of the triangle (base).
        h (float): Height of the triangle.

    Returns:
        float: Area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive.")
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Expected output: 7.5
print(triangle_area(10, 5))  # Expected output: 25.0
print(triangle_area(0, 3))   # Expected output: ValueError
print(triangle_area(5, 0))   # Expected output: ValueError
```