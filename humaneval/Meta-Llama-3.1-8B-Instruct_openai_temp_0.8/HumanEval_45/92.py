```python
def triangle_area(a, h):
    """
    Given length of a base side and high return area for a triangle.
    
    Parameters:
    a (float): The base length of the triangle.
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

This script defines a function `triangle_area` that takes the base length `a` and height `h` of a triangle as input, calculates the area using the formula `(base * height) / 2`, and returns the result. The example usage at the end demonstrates how to use the function to find the area of a triangle with base length 5 and height 3.