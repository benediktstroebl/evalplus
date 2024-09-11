### Calculating Triangle Area
```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.

    Parameters:
    a (float): base of the triangle
    h (float): height of the triangle

    Returns:
    float: area of the triangle

    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Example usage:
print(triangle_area(5, 3))
```
This Python script defines a function `triangle_area` that calculates the area of a triangle given its base `a` and height `h`. The function uses the formula for the area of a triangle, which is `(base * height) / 2`. The script also includes a docstring that explains how to use the function and provides an example usage.