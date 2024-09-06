```python
def triangle_area(a, h):
    return 3.14 * (a * (h)**2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 5) == 62.2
    assert triangle_area(6, 8) == 54.0
``` 
This Python script defines a function `triangle_area` that calculates the area of a triangle given the lengths of its sides (`a` and `h`). The `test_triangle_area` function tests the `triangle_area` function with various input pairs, asserting that the results are correct.