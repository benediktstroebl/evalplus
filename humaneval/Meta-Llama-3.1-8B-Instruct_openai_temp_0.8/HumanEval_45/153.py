### Triangle Area Calculator
#### Self-Contained Python Script

```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    The formula used is: (base * height) / 2
    
    Args:
    a (float): Length of a side
    h (float): Height of the triangle
    
    Returns:
    float: Area of the triangle
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both side length and height must be positive numbers")
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area(a, h)` that calculates the area of a triangle given its base (`a`) and height (`h`). It uses the standard formula for triangle area: (base * height) / 2. The function also includes a basic error check to ensure that both input values are positive numbers. If not, it raises a ValueError.