```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    The area of a triangle is calculated using the formula: area = 0.5 * base * height.
    
    Args:
        a (float): The length of the side of the triangle.
        h (float): The height of the triangle.
    
    Returns:
        float: The area of the triangle.
    
    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Testing the function
print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(10, 5)) # Output: 25.0
```

This script defines a function `triangle_area` that calculates the area of a triangle given the length of one side and the height. The area is calculated using the formula: area = 0.5 * base * height. The script also includes example usage of the function.