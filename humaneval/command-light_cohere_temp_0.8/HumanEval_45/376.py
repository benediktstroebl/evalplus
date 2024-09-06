```python
def triangle_area(a, h):
    return 3 * (a**2 + h**2) ** 0.5

def test_triangle_area():
    assert triangle_area(5, 3) == 7.25, "Assertion fails for given inputs"
    assert triangle_area(4, 4) == 16.0, "Assertion fails for given inputs"
    assert triangle_area(7, 7) == 56.0, "Assertion fails for given inputs"
```
This code defines a function `triangle_area` that calculates the area of the triangle. It also provides a function `test_triangle_area` to test the function's correctness with some input values.