```python
def triangle_area(a, h):
    """
    Calculates the area of the triangle given its sides.
    Args:
        a (length of the side)
        h (height of the triangle)
    Returns:
        float: The area of the triangle
    """
    # Using Heron's formula to calculate the area
    return sqrt(sine(a)*sine(h-a)*sine(h)) / 2)

# Unit tests
def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 12) == 50.2
    assert triangle_area(0.2, 0.5) == 0.0
```