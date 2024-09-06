```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 40.0
    assert triangle_area(6, 8) == 56.0
```
This script provides a self-contained function `triangle_area` that calculates the area of the triangle with the given base and height. It also provides a test function `test_triangle_area` to check the correctness of the `triangle_area` function.