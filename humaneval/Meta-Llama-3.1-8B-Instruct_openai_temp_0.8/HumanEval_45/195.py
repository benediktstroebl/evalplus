```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    The formula used is (base * height) / 2, treating 'a' as the base.

    Args:
        a (float): The length of the side of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that takes two arguments, `a` and `h`, representing the length of a side and the height of the triangle, respectively. The function uses the formula `(base * height) / 2` to calculate the area of the triangle, treating `a` as the base. It then includes a test case to verify the function's correctness.