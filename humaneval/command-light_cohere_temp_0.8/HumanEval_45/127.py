```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 40.2
    assert triangle_area(6, 8) == 56
    assert triangle_area(12, 13) == 113
```

This script defines a function `triangle_area` that calculates the area of the triangle using the formula A = (a * (h + a) / 2)) where `a` and `h` are the lengths of the sides of the triangle. The `test_triangle_area` function tests the function with the provided inputs and asserts the output of the `triangle_area` function with the correct result.