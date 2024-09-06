```python
def triangle_area(a, h):
    return 3.0 * (a** / 2.0) **area(a, h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 8) == 40.0
``` 
The script defines a function `triangle_area` that calculates the area of a triangle with given sides. The `test_triangle_area` function tests the `triangle_area` function by passing different values for the `a` and `h` variables and asserting that the function returns the correct result.