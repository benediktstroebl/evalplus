```python
def triangle_area(a, h):
    """
    Given length of a side 'a' and height 'h', return the area of a triangle.

    The formula used is:
    area = 0.5 * base * height

    Args:
        a (float): The base of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h
```

This script defines a function `triangle_area` that takes the base `a` and height `h` of a triangle as input, and returns the area of the triangle using the formula `0.5 * base * height`. The example usage is also included in the docstring for clarity.