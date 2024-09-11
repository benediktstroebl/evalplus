```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.
    
    Parameters:
    a (float): Length of a side
    h (float): Height of the triangle
    
    Returns:
    float: Area of the triangle
    
    Examples:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that takes the length of a side (`a`) and the height (`h`) of a triangle as inputs and returns its area. The formula used to calculate the area is `0.5 * a * h`, which is the standard formula for the area of a triangle. The script includes a docstring to explain what the function does and includes a test case to verify its correctness.