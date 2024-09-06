```python
def triangle_area(a, h):
    """
    Calculate the area of the triangle given the base and height.
    Args:
    a: float, length of the base of the triangle
    h: float, height of the triangle
    Returns: float, area of the triangle
    """
    return 0.5 * (a * (h) ** 0.25
```

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 6) == 62.5
    assert triangle_area(8, 8) == 55.2
    ```