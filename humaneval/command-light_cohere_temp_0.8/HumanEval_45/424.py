```python
def triangle_area(a, h):
    return 3.14159 * (a**h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 4) == 12.28
    assert triangle_area(10, 5) == 65.28
```

The provided Python script defines a function called `triangle_area` that calculates the area of the triangle based on the given two sides. It also includes a test function `test_triangle_area` which asserts that the function `triangle_area` correctly computes the area of the triangle with the given sides.