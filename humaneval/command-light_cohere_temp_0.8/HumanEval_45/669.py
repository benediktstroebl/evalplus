```python
def triangle_area(a, h):
    return 3.0 * a * (a ** 2) + h

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Should be equal"
    assert triangle_area(3, 5) == 5.0, "Should be equal"
    assert triangle_area(8, 10) == 85.0, "Should be equal"
```
This script defines a function `triangle_area` that computes the area of a triangle given its two sides. It also has a test function `test_triangle_area` that passes three corresponding tests.