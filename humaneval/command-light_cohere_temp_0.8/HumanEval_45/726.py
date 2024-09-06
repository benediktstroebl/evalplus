```python
def triangle_area(a, h):
    return (a * (h + a) / 2) ** .5

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 5) == 52
    assert triangle_area(8, 12) == 104
    assert triangle_area(3, 1) == 6.2
```