```python
def triangle_area(a, h):
    return 3.14 * a * (a**2 + h**2) / 2

def test_triangle_area():
    assert triangle_area(5, 3) == 7.14 * (5**2 + 3**2) / 2 == 7.5
```