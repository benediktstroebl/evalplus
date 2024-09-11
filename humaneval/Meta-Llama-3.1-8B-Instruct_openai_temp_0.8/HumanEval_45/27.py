### Triangle Area Calculator

Here's a simple Python function that calculates the area of a triangle given its base length `a` and height `h`.

```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    Args:
        a (float): The base length of the triangle.
        h (float): The height of the triangle.

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

This function uses the formula for the area of a triangle: `A = (1/2) * base * height`. It takes the base `a` and height `h` as arguments, calculates the area, and returns the result. The example given in the docstring demonstrates how to use the function.