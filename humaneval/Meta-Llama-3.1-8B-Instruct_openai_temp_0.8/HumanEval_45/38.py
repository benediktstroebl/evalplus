### Triangle Area Calculator
```python
def triangle_area(a, h):
    """
    Given length of a side (base) and high (height) return area for a triangle.

    Args:
        a (float): Length of the side (base) of the triangle.
        h (float): Height of the triangle.

    Returns:
        float: Area of the triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both side and height must be positive numbers")
    return 0.5 * a * h

# Example usage
print(triangle_area(5, 3))  # Output: 7.5
```
This script defines a function `triangle_area` that calculates the area of a triangle given its base and height. It includes a docstring with examples, input validation, and an example usage section at the end.