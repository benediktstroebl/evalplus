```python
def triangle_area(a, h):
    return a * (h / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 4) == 8
    assert triangle_area(13, 15) == 178
```

This Python code defines a function `triangle_area` that calculates the area of the triangle given the base `a` and height `h`. The function returns the calculated area. It also includes a test function `test_triangle_area` that tests the `triangle_area` function with different inputs.