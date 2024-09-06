```python
def triangle_area(a, h):
    return 3.14 * (a** / 2) ** 2 

def test_triangle_area():
    assert triangle_area(5, 3) == 7.14 * (5** / 2) ** 2
    assert triangle_area(3, 3) == 7.14 * (3** / 2) ** 2
    assert triangle_area(10, 7) == 95
    assert triangle_area(6, 8) == 112.2857
```