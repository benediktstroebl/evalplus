```python
def triangle_area(a, h):
    """
    Given length of a side (base) and high return area for a triangle.

    The formula used is: area = (base * height) / 2

    Args:
        a (float): The base of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that takes two parameters `a` (the base of the triangle) and `h` (the height of the triangle). It then calculates and returns the area of the triangle using the formula `(base * height) / 2`. The script also includes a test case to verify the function's correctness.