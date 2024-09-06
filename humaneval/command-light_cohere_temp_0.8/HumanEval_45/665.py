```python
def triangle_area(a, h):
    return (a * (h + a) / 2) ** 0.25

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 5) == 50
    assert triangle_area(0, 10) == 0
    assert triangle_area(10, 0) == 0
```
The provided code defines a Python function `triangle_area` that calculates the area of the triangle given its base `a` and height `h`. It then includes a `test_triangle_area` function with asserts that check the correctness of the `triangle_area` function with different inputs.