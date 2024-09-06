```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 8) == 40.0
    assert triangle_area(10, 5) == 50.0
```
The provided Python code defines a function `triangle_area` that calculates the area of a triangle based on the provided lengths of its sides. It then includes a test function `test_triangle_area` that asserts the function's correctness by passing different inputs and comparing the returned area values.