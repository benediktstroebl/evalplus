```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height return area for a triangle.

    Args:
        a (float): Base of the triangle.
        h (float): Height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that takes two arguments, `a` and `h`, which represent the base and height of a triangle respectively. The function returns the area of the triangle using the formula `0.5 * base * height`. The script also includes a docstring to provide documentation for the function and an example usage of the function.