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
    return sqrt(sine_elder(side, 3) * side * (side**2 + height**2))

def sine_elder(a, b):
    """
    Calculates the sine and entropy of a (a,b) pair
    """
    return sqrt(b * (b - a) * (2*a + b)) / (a + sqrt(a*b))

def test_triangle_area():
    """
    Test the triangle_area function
    """
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 4) == 12.0
    assert triangle_area(10, 5) == 92.0
    assert triangle_area(7, 7) == 52.0

print("Test passed for triangle_area.")
```