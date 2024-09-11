```python
def triangle_area(a, h):
    """
    Given length of a side (base) and high return area for a triangle.
    
    Args:
        a (float): The length of the base of the triangle.
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

This Python script defines a function `triangle_area` that calculates the area of a triangle given the length of its base (`a`) and its height (`h`). The function uses the formula for the area of a triangle, which is `(base * height) / 2`. The result is returned by the function. The script includes a docstring that explains how to use the function and includes a test case to demonstrate its usage.