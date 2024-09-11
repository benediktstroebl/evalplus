```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height return the area for a triangle.

    The formula used for the area of a triangle is: area = (base * height) / 2

    Args:
        a (float): Length of the side (base) of the triangle.
        h (float): Height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))
```

In this script, the `triangle_area` function takes two parameters, `a` and `h`, representing the base and height of a triangle, respectively. It returns the area of the triangle using the formula `area = (base * height) / 2`. The script also includes a test case to demonstrate the function's usage.