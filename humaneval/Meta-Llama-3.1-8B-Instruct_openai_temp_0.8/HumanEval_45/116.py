```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    
    The area of a triangle is calculated using the formula: 
    Area = (base * height) / 2
    
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
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that takes the base `a` and the height `h` of a triangle as input, and returns the area of the triangle. The area is calculated using the formula `(base * height) / 2`. The script also includes a test case to verify that the function works correctly.