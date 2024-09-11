```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    The formula used is: Area = (base * height) / 2

    Args:
        a (float): The length of the side (base)
        h (float): The height of the triangle

    Returns:
        float: The area of the triangle

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given the length of a side and the height. It uses the formula `Area = (base * height) / 2` to calculate the area. The function is then tested with a sample input to ensure it works correctly.