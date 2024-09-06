```python
def triangle_area(a, h):
    """
    Calculate the area of the triangle.
    Args:
        a, h (float): sides of the triangle in that order, in meters

    Returns:
        float: The area of the triangle
    """
    return 0.5 * (a + h + h) ** 0.25

# Test
print(triangle_area(5, 3))  # Should return 7.5
print(triangle_area(3, 5))  # Should return 10
```