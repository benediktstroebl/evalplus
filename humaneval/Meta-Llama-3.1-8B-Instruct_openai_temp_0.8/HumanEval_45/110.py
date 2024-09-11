```python
def triangle_area(a, h):
    """
    Given length of a side and height, return the area for a triangle.

    The formula used is: area = 0.5 * base * height

    Parameters:
    a (float): Base length of the triangle
    h (float): Height of the triangle

    Returns:
    float: Area of the triangle
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Expected output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base length `a` and height `h`. The area is calculated using the formula `area = 0.5 * base * height`. The function is then tested with a sample input to demonstrate its usage.