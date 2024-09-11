```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h), 
    returns the area of a triangle.

    Args:
        a (float): The length of one side of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.
    """
    if a <= 0 or h <= 0:
        raise ValueError("Side length and height must be positive.")

    area = 0.5 * a * h
    return area

# Test the function
print(triangle_area(5, 3))  # Expected output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base (`a`) and height (`h`). It first checks if both `a` and `h` are positive, raising a `ValueError` if they are not. It then calculates the area using the formula `area = 0.5 * a * h` and returns it. The test at the end of the script verifies that the function works correctly for the given example.