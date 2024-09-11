### Triangle Area Calculator
```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.
    
    Parameters:
    a (float): length of a side
    h (float): height of the triangle
    
    Returns:
    float: area of the triangle
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```
This script defines a function `triangle_area` that calculates the area of a triangle given its side length `a` and height `h`. The area is calculated using the formula `A = 0.5 * base * height`, where `A` is the area of the triangle. The function includes a docstring that explains its purpose, parameters, and return value. The script also includes an example usage of the function.