```python
def triangle_area(a, h):
    return (a * (h + a) ) / 2

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(4, 8) == 22.0
    assert triangle_area(6, 4) == 12.0
```