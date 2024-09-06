```python
def triangle_area(a, h):
    """
    Calculates the area of the triangle given its sides.
    Args:
        a (float), b (float), h (float)
    Returns:
        float: The area of the triangle
    """
    return 0.5 * (a + h + h) ** 0.25

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 8) == 40
    assert triangle_area(10, 5) == 62.5

test_triangle_area()
```