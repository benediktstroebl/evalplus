### Calculating Triangle Area
```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.
    
    Formula used: Area = (base * height) / 2
    
    Args:
        a (float): Length of a side.
        h (float): Height of the triangle.
    
    Returns:
        float: Area of the triangle.
    
    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```