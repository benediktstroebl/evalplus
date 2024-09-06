```python
def triangle_area(a, h):
    return 0.25 * h * a * a

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Should return area of triangle with sides 5 and 3"
```
The function `triangle_area` calculates the area of a triangle using the formula 0.25 * h * a base. The function is then tested to pass the test using the `test_triangle_area` function.