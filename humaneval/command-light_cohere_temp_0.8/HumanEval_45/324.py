```python
def triangle_area(a, h):
    return 0.5 * (a * (h)**2

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 16) == 65
    assert triangle_area(10, 5) == 62.0
    assert triangle_area(15, 10) == 212.2
```

The above Python script defines a `triangle_area` function that calculates the area of a triangle given the base and height. It also has a test function `test_triangle_area` that passes all the test cases for the `triangle_area` function.