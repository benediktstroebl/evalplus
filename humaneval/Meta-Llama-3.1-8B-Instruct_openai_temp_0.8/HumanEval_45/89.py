```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    The area of a triangle is calculated using the formula:
    area = (base * height) / 2
    In this case, base is given as 'a' and height as 'h'.

    Args:
        a (float): The length of the base of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2

# Test the function
assert triangle_area(5, 3) == 7.5
print("Function works as expected.")
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base and height. It uses the formula for the area of a triangle, which is `(base * height) / 2`. The script also includes an example use case and a test to ensure the function works as expected.