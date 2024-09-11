```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.

    The formula used is: area = (a * h) / 2

    Args:
        a (float): length of a side
        h (float): height of the triangle

    Returns:
        float: area of the triangle

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both side length and height must be positive.")
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that takes two arguments, `a` and `h`, representing the side length and height of a triangle, respectively. It calculates and returns the area of the triangle using the formula `(a * h) / 2`. It also includes a docstring with examples and error checking to ensure that both the side length and height are positive.