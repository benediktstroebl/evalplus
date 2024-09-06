```python
def triangle_area(a, h):
    """
    Calculate the area of the triangle given the base and height.
    Args:
        a: float, base length of the triangle
        h: float, height of the triangle
    Returns:
        float, area of the triangle
    """
    return 0.5 * (a * (h) ** 0.25
```

def test_triangle_area():
    assert triangle_area(5., 3.)print("Passed test!")

test_triangle_area()
```