```python
def triangle_area(a, h):
    return 3.14 * (a * (h)**2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 62.5
    assert triangle_area(8, 6) == 56.25
```