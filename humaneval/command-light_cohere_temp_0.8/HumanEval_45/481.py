```python
def triangle_area(a, h):
    return 3.14159 * (a**h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 5) == 62.25
    assert triangle_area(8, 10) == 89.4
```

This script defines a function that calculates the area of a triangle using the formula for the area of a triangle (a * (b * h)), and then tests this function with three different inputs and asserts.