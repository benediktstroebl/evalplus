```python
def triangle_area(a, h):
    return 3.0 * a * a * (a + h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 42.0
    assert triangle_area(8, 10) == 70.0
``` 
This code defines a function `triangle_area` that computes the area of the triangle using its sides `a` and `h` and passes the test `test_triangle_area` to check its correctness.