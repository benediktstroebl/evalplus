```python
def triangle_area(a, h):
    return 3.14159 * (a ** (h)**0.25)
```
```
def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 6) == 28.8
    assert triangle_area(0, 0) == 0
    assert triangle_area(5, 1) == .25001
    assert triangle_area(6, -1) == 0
```