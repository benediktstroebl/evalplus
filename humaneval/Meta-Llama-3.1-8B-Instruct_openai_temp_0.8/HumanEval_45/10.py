```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height return area for a triangle.
    
    The formula used for the area of a triangle is: Area = (base * height) / 2
    
    Parameters:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    >>> triangle_area(5, 3)
    7.5
    """
    if a < 0 or h < 0:
        raise ValueError("Input values must be non-negative.")
    return (a * h) / 2

# Example usage
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that takes two parameters, `a` (the base of the triangle) and `h` (the height of the triangle), and returns the area of the triangle. The area is calculated using the formula `Area = (base * height) / 2`. The script also includes input validation to ensure that the base and height are non-negative.