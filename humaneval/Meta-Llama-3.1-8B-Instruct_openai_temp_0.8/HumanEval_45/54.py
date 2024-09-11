```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height return area for a triangle.
    
    The formula for the area of a triangle is (base * height) / 2.
    
    Parameters:
    a (float): length of the base (side) of the triangle
    h (float): height of the triangle
    Returns:
    float: area of the triangle
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive numbers")
    
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given the length of its base and height. The function includes a check to ensure that both the base and height are positive numbers. It also includes a docstring that explains the purpose of the function, its parameters, and its return value. The script then tests the function with an example.