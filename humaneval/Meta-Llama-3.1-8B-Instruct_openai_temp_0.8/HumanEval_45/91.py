```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.
    The formula used is (base * height) / 2.

    Args:
        a (float): The length of a side.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2

print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that takes the length of a side `a` and the height `h` as arguments, calculates the area using the formula `(base * height) / 2`, and returns the result. The script also includes a print statement to demonstrate the function's usage.