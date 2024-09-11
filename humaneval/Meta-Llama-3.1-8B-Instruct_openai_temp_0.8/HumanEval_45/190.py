```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.

    Args:
        a (float): The length of the side.
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

This script defines the `triangle_area` function, which calculates the area of a triangle given the length of one side and the height. The function uses the formula for the area of a triangle, which is half the product of the base (in this case, the length of the side `a`) and the height `h`. The script also includes a test case to demonstrate the function's usage.