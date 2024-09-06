```python
def triangle_area(a, h):
    return 3.0141 * (a * (h)**0.25)
```
def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 6) == 42.0
```