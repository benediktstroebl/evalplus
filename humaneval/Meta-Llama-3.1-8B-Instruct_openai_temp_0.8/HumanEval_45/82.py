```python
def triangle_area(a, h):
    """
    Given length of a side (a) and the height (h) return area for a right triangle.
    
    The formula used is Area = (base * height) / 2
    
    Parameters:
    a (float): The length of the base side of the triangle.
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

This script defines a function `triangle_area` that calculates the area of a right triangle given the length of the base `a` and the height `h`. It then tests the function with the provided example.