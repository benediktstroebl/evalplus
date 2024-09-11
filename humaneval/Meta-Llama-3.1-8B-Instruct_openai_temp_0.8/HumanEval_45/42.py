```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    The formula used for calculating the area of a triangle is (base * height) / 2.
    Since the problem statement specifies that 'a' is the side and 'h' is the height,
    we will treat 'a' as the base and 'h' as the height for the calculation.

    Args:
        a (float): The length of the base of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    area = (a * h) / 2
    return area

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that calculates the area of a triangle given the base and height. It then tests the function with the example provided in the problem statement. The formula used is the standard formula for the area of a triangle, which is `(base * height) / 2`.