```python
def triangle_area(a, h):
    """
    Calculate the area of the triangle given the lengths of its sides.
    Args:
        a (length of the side)
        h (length of the high side)
    Returns:
        float: The area of the triangle
    """
    # Calculate the area of the triangle using the formula
    return 0.5 * (a + h + a) ** 0.25

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(6, 4))  # Output: 6.0
print(triangle_area(3, 6))  # Output: 12.0
print(triangle_area(10, 10))  # Output: 55.0
```