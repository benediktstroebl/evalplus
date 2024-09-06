```python
def triangle_area(a, h):
    return 3.0 * a * a * h

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 6) == 126.0
```

This Python code defines a function `triangle_area` that calculates the area of a triangle given the length of its sides (`a` and `h`). The function uses the formula for the area of a triangle, which is `0.0 * a base * height` to calculate the area. The code also includes a `test_triangle_area` function, which tests whether the `triangle_area` function correctly calculates the area of a triangle with given side lengths.