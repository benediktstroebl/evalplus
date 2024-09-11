```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.

    Parameters:
    a (float): The base length of the triangle.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.

    Examples:
    >>> triangle_area(5, 3)
    7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be greater than 0.")
    return 0.5 * a * h

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that takes two parameters, `a` and `h`, which represent the base and height of a triangle respectively. The function calculates the area of the triangle using the formula `0.5 * base * height` and returns the result. If either `a` or `h` is not greater than 0, it raises a `ValueError` to ensure that both base and height are valid for a triangle. Finally, it demonstrates how to use the function with an example.