```python
def triangle_area(a, h):
    return 3.14 * (a * (h) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 12.14
    assert triangle_area(7, 7) == 28.5
    assert triangle_area(8, 9) == 55.66
```

This Python script defines a function `triangle_area` that calculates the area of a triangle based on the provided side length and high. It also provides a test function `test_triangle_area` to pass all the corresponding tests for the `triangle_area` function.