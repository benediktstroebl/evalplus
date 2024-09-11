```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    Parameters:
    a (float): length of the base side
    h (float): height of the triangle

    Returns:
    float: area of the triangle
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Should return 7.5
```

This script defines a function `triangle_area` that takes in the base side length `a` and the height `h` of a triangle, and returns the area of the triangle. The area of a triangle can be calculated using the formula `0.5 * base * height`, which is implemented in the function. The script also includes a test case to verify that the function is working correctly.