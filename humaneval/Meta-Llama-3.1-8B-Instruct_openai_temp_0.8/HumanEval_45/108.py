### Triangle Area Calculator
```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.

    The formula used is: area = (base * height) / 2

    Args:
        a (float): The length of the side (base) of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both side and height must be positive.")
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```
This script defines a function `triangle_area` that calculates the area of a triangle given the length of a side (base) and the height. It includes a docstring that explains the formula used, the function's parameters, and its return value. The script also includes a brief example of how to use the function and tests it with a specific input.