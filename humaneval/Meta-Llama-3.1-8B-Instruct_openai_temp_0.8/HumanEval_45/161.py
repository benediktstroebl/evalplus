```python
# Define a function to calculate the area of a triangle
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.
    
    Parameters:
    a (float): Length of a side of the triangle.
    h (float): Height of the triangle.
    
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

This script defines a function `triangle_area` that takes two parameters, `a` (the length of a side) and `h` (the height), and returns the area of the triangle. The area of a triangle is given by the formula `0.5 * base * height`, and this function calculates and returns this value. The script then tests the function with an example.