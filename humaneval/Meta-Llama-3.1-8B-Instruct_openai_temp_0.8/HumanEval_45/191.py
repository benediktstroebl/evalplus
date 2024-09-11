```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height return area for a triangle.

    The area of a triangle is calculated using the formula: area = (base * height) / 2

    Args:
        a (float): The base of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that takes two arguments, `a` (the base) and `h` (the height), and returns the area of the triangle using the formula `area = (base * height) / 2`. The function is then tested with the example provided in the docstring.