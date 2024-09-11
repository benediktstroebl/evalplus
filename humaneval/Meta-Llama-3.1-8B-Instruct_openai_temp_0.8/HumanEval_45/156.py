```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    The side given is assumed to be the base of the triangle.

    Args:
        a (float): The base of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a `triangle_area` function that calculates the area of a triangle given its base (`a`) and height (`h`). The function uses the formula for the area of a triangle, which is 0.5 times the base times the height. The script also includes a docstring with a description of the function, its arguments, and its return value, as well as an example usage. Finally, the script tests the function with an example call.