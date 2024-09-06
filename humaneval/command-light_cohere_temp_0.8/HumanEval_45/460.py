```python
def triangle_area(a, h):
    return (a * (h + a) ) / 2

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 10) == 55
    assert triangle_area(4, 6) == 10
    assert triangle_area(10, 4) == 22.5
```
The provided Python script defines a function `triangle_area` that calculates the area of a triangle with two sides of length `a` and `h` using the formula `(a * (h + a) ) / 2)`. The `test_triangle_area` function contains several assert statements that check the correctness of the `triangle_area` function with different input values. The code is a self-contained and efficient way of calculating the area of the triangle.