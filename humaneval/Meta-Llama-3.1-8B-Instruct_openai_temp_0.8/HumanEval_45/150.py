```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    The formula used to calculate the area of the triangle when the base (a) and height (h) are known is:

    Area = (base * height) / 2

    Args:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.

    Examples:
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Test the function with a known example
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area(a, h)` that takes two arguments, `a` and `h`, which represent the base and height of a triangle respectively. The function returns the area of the triangle using the formula `(base * height) / 2`. The script also includes docstrings and example usage to demonstrate how to use the function and ensure it works as expected.