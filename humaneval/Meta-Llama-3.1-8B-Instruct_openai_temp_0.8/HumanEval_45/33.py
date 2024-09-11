```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    The area of a triangle can be calculated using the formula:
    area = 0.5 * base * height

    Parameters:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.

    >>> triangle_area(5, 3)
    7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive.")
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that takes the base (`a`) and height (`h`) of a triangle as input and returns its area. It also includes a check to ensure that both the base and height are positive, as a triangle cannot have a negative or zero base or height. Finally, it includes a test case to demonstrate the function's usage.