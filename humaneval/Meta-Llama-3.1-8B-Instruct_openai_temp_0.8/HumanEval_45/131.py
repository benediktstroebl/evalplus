```python
def triangle_area(a, h):
    """
    Given length of a side (base) and high (height) return area for a triangle.
    
    Args:
        a (float): The length of the base of the triangle.
        h (float): The height of the triangle.
        
    Returns:
        float: The area of the triangle.
        
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given the base length `a` and height `h`. The function uses the formula for the area of a triangle (0.5 * base * height) to compute the result. The example usage at the end demonstrates how to call the function with specific values for `a` and `h`.