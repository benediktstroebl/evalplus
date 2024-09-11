```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.

    Args:
        a (float): The length of the side of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Testing the function
print(triangle_area(5, 3))
```

This Python script defines a function `triangle_area` that calculates the area of a triangle given the length of a side and its height. It also includes a docstring to describe the function and its parameters. The script then prints the result of `triangle_area(5, 3)` to demonstrate its usage.