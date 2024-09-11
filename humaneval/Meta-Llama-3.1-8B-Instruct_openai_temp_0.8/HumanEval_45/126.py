```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    Args:
        a (float): Length of a side.
        h (float): Height of the triangle.

    Returns:
        float: Area of the triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Side and height must be positive numbers.")
    return 0.5 * a * h

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function called `triangle_area` which calculates the area of a triangle given its base (or side) and height. It also includes a check to ensure that both the base and height are positive numbers, raising an error if they are not. The function uses the formula for the area of a triangle, which is half the product of its base and height. 

The example usage at the end of the script demonstrates how to use this function with the provided example inputs.