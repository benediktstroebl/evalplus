```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.

    The formula to calculate the area of a triangle is: area = (base * height) / 2

    Args:
        a (float): The length of the side of the triangle (also the base).
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

In this script, we define a function `triangle_area` that takes two arguments, `a` (the length of the side) and `h` (the height). The function uses the formula for the area of a triangle (`area = (base * height) / 2`) and returns the calculated area. We then test the function with the example provided in the docstring.