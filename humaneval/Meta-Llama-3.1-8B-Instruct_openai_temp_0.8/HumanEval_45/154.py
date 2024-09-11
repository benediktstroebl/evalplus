### Triangle Area Calculator
```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.

    Args:
        a (float): Length of a side
        h (float): Height of the triangle

    Returns:
        float: Area of the triangle

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(10, 4))  # Output: 20.0
```

This script defines a function `triangle_area` that takes the length of a side `a` and the height `h` of a triangle as input and returns the area of the triangle. The area is calculated using the formula `0.5 * a * h`, where `a` is the length of the base and `h` is the height of the triangle. The script also includes docstrings to provide documentation for the function and examples of how to use it.