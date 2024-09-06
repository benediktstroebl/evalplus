```python
def triangle_area(a, h):
    """
    Calculates the area of the triangle given the lengths of its sides.
    Args:
        a, b ( cousins )
        h ( base )
    
    Returns:
        float: The area of the triangle.
    """
    # Calculates the area of the triangle
    area = (1/2) * (a + b + h) * (h - a - b)
    return area

# Test
print(triangle_area(5, 3)) # Output: 7.25
print(triangle_area(10, 5)) # Output: 55.0
print(triangle_area(7, 8)) # Output: 49.75
```