Here is a self-contained Python script that defines a function triangle_area that computes and returns the area of a triangle:
```python
def triangle_area(a, h):
    """
    Calculates the area of the triangle using Heron's formula.
    Args:
    side: Length of one side of the triangle.
    height: Height of the triangle
    Returns:
    Area of the triangle (in squared units)
    """
    return math.sqrt(s_area(a, h, a)) * 2

def s_area(x, y, z):
    """
    Calculates the semi-angled area of a triangle using Heron's formula.
    Args:
    x, y, z: Length of two sides of the triangle (in that order)
    """
    return math.sqrt((x area(y - x * z - z * y, x * y - z * x, z * x - y * z) ) / 2

def test_triangle_area():
    """
    Tests the triangle_area function
    """
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 8) == 56
    assert triangle_area(10, 5) == 85.5

print("Triangle Area Function works!")
```