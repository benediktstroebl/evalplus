### Python Script for Calculating Triangle Area
```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.

    The area of a triangle is calculated using the formula: area = (base * height) / 2
    In this case, the base is the given side length 'a' and the height is 'h'.

    Args:
        a (float): Length of the side.
        h (float): Height of the triangle.

    Returns:
        float: Area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that takes the length of a side `a` and the height `h` as input and returns the area of the triangle. The area is calculated using the formula `area = (base * height) / 2`. The function includes a docstring that provides a description, explains the formula, and includes an example usage. The script also includes a test call to the function to demonstrate its usage.