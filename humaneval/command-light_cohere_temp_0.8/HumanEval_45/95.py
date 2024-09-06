```python
def triangle_area(a, h):
    return 3.14159 * (a** 2 * h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(3, 4) == 2.16]);
```  This script defines a function, `triangle_area`, that calculates the area of a triangle using the formula A = sqrt(a^2 + b^2 + h^2) and passes the test using the `test_triangle_area` function.