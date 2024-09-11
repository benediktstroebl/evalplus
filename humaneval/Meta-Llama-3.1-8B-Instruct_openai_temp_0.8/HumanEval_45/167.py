```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    The area of a triangle can be calculated using the formula:
    Area = (base * height) / 2

    Parameters:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.

    Examples:
    >>> triangle_area(5, 3)
    7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive")
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Expected output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base and height. It includes a check to ensure that both the base and height are positive. The function is then tested with a sample input.