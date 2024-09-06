```python
def triangle_area(a, h):
    return 3.0 * a * (a**2) / 2

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 6) == 38.2
    assert triangle_area(12, 13) == 109.0
```