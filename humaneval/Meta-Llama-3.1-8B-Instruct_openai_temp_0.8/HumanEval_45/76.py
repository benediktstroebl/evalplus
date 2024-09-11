```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.

    Parameters:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """
    area = 0.5 * a * h
    return area

# Test the function
print(triangle_area(5, 3))  # Expected output: 7.5
```

This script defines a `triangle_area` function that calculates the area of a triangle given its base length `a` and height `h`. The area is calculated using the formula `0.5 * base * height`. The function then tests the calculation with the example given in the problem description.