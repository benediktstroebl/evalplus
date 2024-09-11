```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    The area of a triangle is calculated as half the product of the base (side 'a') and the height 'h'.
    
    Parameters:
    a (float): The length of a side.
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

This script defines a function `triangle_area` that takes two parameters, `a` (the length of a side) and `h` (the height of the triangle), and returns the area of the triangle. The area is calculated using the formula `0.5 * a * h`. The script also includes a test case to demonstrate the function's usage.