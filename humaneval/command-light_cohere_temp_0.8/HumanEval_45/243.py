```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(3, 5) == 12.0
    assert triangle_area(10, 10) == 100.0
```

This script defines a function called `triangle_area` that calculates the area of the triangle using the formula (a * (h + a) / 2) and passes the corresponding tests.