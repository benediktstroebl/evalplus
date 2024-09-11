```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    Args:
        a (float): The length of a side.
        h (float): The height of the triangle.
    
    Returns:
        float: The area of the triangle.
    
    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    # The formula to calculate the area of a triangle is (base * height) / 2
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Expected output: 7.5
```

This script defines a function `triangle_area` that takes the base `a` and height `h` of a triangle as arguments and returns the area. It includes a docstring that explains the purpose of the function, its arguments, return value, and provides an example usage. The function uses the formula for the area of a triangle, and the script includes a test case to verify its correctness.