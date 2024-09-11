```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.

    The area of a triangle is calculated by (base * height) / 2.
    Here, the side of the triangle is considered as the base and height is given as input.

    Args:
        a (float): Length of the side of the triangle (base).
        h (float): Height of the triangle.

    Returns:
        float: Area of the triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2

# Test the function
if __name__ == "__main__":
    print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base (side) and height. The function uses the formula `(base * height) / 2` to calculate the area. The script also includes a test case to verify the function's correctness.