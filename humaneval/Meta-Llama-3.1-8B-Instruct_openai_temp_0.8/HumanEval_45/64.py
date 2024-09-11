```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    The area of a triangle is calculated as (base * height) / 2.
    In the context of this function, 'a' is considered the base.

    Args:
        a (float): The length of the base of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive numbers")
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that takes the length of the base (`a`) and the height (`h`) of a triangle as input and returns the area of the triangle. It includes a docstring that describes the function's behavior, parameters, and return value. The example usage in the docstring is also tested at the end of the script. The function raises a `ValueError` if the base or height is not a positive number.