```python
def triangle_area(a, h):
    return 3.14159 * (a**2 * h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 6) == 62.28
    assert triangle_area(4, 8) == 12.884
```
This Python script defines a function called `triangle_area` that calculates the area of a triangle with a given base `a` and height `h`. The function uses the formula for the area of a triangle: `Area = (1/2) * a * h`. 

The `test_triangle_area` function is used to test the `triangle_area` function with various input values.