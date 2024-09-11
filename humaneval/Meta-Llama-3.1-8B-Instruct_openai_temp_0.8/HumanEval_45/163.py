```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.

    Parameters:
    a (float): length of the side
    h (float): height of the triangle

    Returns:
    float: area of the triangle

    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

print(triangle_area(5, 3))  # test the function
```

This script defines a function `triangle_area` that calculates the area of a triangle given the length of a side and the height of the triangle. The area is calculated using the formula `0.5 * base * height`. The function includes a docstring that describes its parameters and return value, as well as an example usage. Finally, the script prints the result of calling `triangle_area` with the example parameters.