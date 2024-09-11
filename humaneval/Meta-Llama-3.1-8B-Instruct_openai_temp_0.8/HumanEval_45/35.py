### Calculating the Area of a Triangle
A Python function to calculate the area of a triangle given its side length and height.

```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height return area for a triangle.
    
    Parameters:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    >>> triangle_area(5, 3)
    7.5
    
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive.")
    return 0.5 * a * h

# Example usage:
print(triangle_area(5, 3))
```

This script defines a function `triangle_area(a, h)` that takes two arguments: `a`, the length of the base of the triangle, and `h`, the height of the triangle. It then returns the area of the triangle using the formula `0.5 * a * h`. The function includes error checking to ensure that both the base and the height are positive.