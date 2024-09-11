### Triangle Area Calculator
```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height return area for a triangle.

    The formula used is: area = 0.5 * base * height

    Args:
        a (float): The length of the base of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```
This script defines a function `triangle_area` that takes two arguments, `a` (the base of the triangle) and `h` (the height of the triangle), and returns the area of the triangle. The area is calculated using the formula `0.5 * base * height`. The script also includes a docstring that explains how to use the function and provides an example of how to call it.