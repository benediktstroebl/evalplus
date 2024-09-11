```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.
    The area is calculated using the formula: area = 0.5 * base * height

    Args:
        a (float): Length of the side (base) of the triangle.
        h (float): Height of the triangle.

    Returns:
        float: Area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive numbers.")
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that takes the length of a side (`a`) and the height (`h`) as arguments and returns the area of the triangle. It also includes a docstring that explains the purpose of the function, the arguments it takes, the return value, and provides an example usage. The function includes a validation check to ensure that both the base and height are positive numbers.