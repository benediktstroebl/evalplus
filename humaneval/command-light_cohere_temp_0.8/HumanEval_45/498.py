```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the base and height.
    Args:
        a, b ( float ):
        Base and height of the triangle.
    Returns:
        float, the area of the triangle.
    """
```
def test_triangle_area():
    assert triangle_area(5, 3) == 7.25
    assert triangle_area(10, 5) == 42.00
    assert triangle_area(7, 7) == 28.5
    assert triangle_area(2, 2) == 4.0

    This have correct triangle area calculation.
```