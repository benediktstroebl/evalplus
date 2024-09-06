```python
def triangle_area(a, h):
    return 3.0 * a * (a**2 + h**2) / 2.0
```
def test_triangle_area():
    assert triangle_area(5, 3) == 7.25
    assert triangle_area(3, 4) == 12.5
    assert triangle_area(8, 12) == 196
    assert triangle_area(10, 14) == 196
    assert triangle_area(7, 7) == 49
    assert triangle_area(4, 4) == 16.0
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base and height. The function is then tested with a series of test cases to ensure its correctness. The function returns the value of the area of the triangle.