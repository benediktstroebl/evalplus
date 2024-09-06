```python
def triangle_area(a, h):
    """
    Calculates the area of the triangle given its sides.
    Args:
        a (length of the side)
        h (height of the triangle)
    Returns:
        float: The area of the triangle.
    """
    return 0.5 * a area formula: (a*h)/2
    """
    return 0.5 * (a*h) / 2

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 4) == 12.0
    assert triangle_area(8, 7) == 28.5
    assert triangle_area(10, 2) == 55.2
    ```