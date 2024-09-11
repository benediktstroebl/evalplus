```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    The area of a triangle is calculated using the formula: (base * height) / 2.
    
    Parameters:
    a (float): The base of the triangle.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Expected output: 7.5
```

This script defines a function `triangle_area` that takes the base `a` and height `h` of a triangle as input and returns the area of the triangle. The function uses the formula `(base * height) / 2` to calculate the area. The script also includes a test case to demonstrate the function's correctness.