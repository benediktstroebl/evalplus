```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.

    The formula for the area of a triangle is: area = (base * height) / 2

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

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area(a, h)` which calculates the area of a triangle given its base `a` and height `h`, using the formula area = (base * height) / 2. The function is then tested with a call to `print(triangle_area(5, 3))`.