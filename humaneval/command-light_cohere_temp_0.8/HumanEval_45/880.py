```python
def triangle_area(a, h):
    return 3.14 * (a * (h) ** 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 42.0
    assert triangle_area(4, 5) == 20.0
```