```python
# Define a function to calculate the area of a triangle
def triangle_area(a, h):
    """
    Given length of a side (base) and height, return the area of a triangle.

    Args:
        a (float): The length of the base of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    # Use the formula for the area of a triangle (A = 0.5 * base * height)
    area = 0.5 * a * h
    return area

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that takes the base and height of a triangle as arguments and returns the area. The area is calculated using the formula for the area of a triangle, `A = 0.5 * base * height`. The script then tests the function with a sample input to demonstrate its usage.