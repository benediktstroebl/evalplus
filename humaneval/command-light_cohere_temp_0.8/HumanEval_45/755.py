```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Check: incorrect area calculation"
    assert triangle_area(8, 10) == 41.2, "Check: incorrect area calculation"
```