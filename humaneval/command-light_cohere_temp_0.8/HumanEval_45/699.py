```python
def triangle_area(a, h):
    return 5 * (a**2 + h**2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 50
    assert triangle_area(4, 10) == 40
    assert triangle_area(6, 1) == 31.2
```