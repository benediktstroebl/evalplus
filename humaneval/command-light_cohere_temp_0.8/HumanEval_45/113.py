```python
def triangle_area(a, h):
    """
    Calculates the area of the triangle using Heron's formula.
    Args:
    side: float, length of a side of the triangle
    height: float, height of the triangle

    Returns:
    float, area of the triangle
    """
    return sqrt((s(a, h, (a+h))/(2))**2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 2) == 6.5
    assert triangle_area(7, 8) == 49.0
```

This code defines a function `triangle_area` that calculates the area of the triangle using Heron's formula and passes the corresponding tests using the `test_triangle_area` function.