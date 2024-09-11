```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    Args:
    a (float): The base length of the triangle.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    Examples:
    >>> triangle_area(5, 3)
    7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive numbers.")
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script includes a docstring to explain what the function does, what arguments it takes, what it returns, and some examples of how to use it. It also includes a check to make sure both the base and height are positive numbers, as a triangle can't have a negative area. If either the base or height is not positive, it raises a ValueError with a helpful message.