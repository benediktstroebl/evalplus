```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.

    Parameters:
    a (float): The base of the triangle.
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

This script defines a function `triangle_area` that takes the base `a` and height `h` of a triangle as input and returns their product divided by 2, which is the formula for the area of a triangle. The script then tests the function with the example provided.