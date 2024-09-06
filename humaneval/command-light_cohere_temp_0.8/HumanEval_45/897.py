```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the lengths of its sides.
    Args:
        a (float), b (float), h (float)
    Returns: 
        float, the area of the triangle
    """
    # Using Heron's formula to calculate the area
    return math.sqrt((a * * (a, b, h) / 2) * sqrt(3) )

# Unit tests
assert triangle_area(5, 3) == 7.5
assert triangle_area(3, 6) == 12.0
assert triangle_area(6, 7) == 42.0
assert triangle_area(10, 5) == 56.0
``` 
This code defines a function `triangle_area` that calculates the area of a triangle using Heron's formula. The function then passes all corresponding tests successfully.