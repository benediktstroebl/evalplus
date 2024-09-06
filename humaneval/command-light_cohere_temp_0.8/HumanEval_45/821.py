```python
def triangle_area(a, h):
    return 3.0 * (a + h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Assertion failed: incorrect triangle area calculation"
    assert triangle_area(8, 10) == 40.0, "Assertion failed: incorrect triangle area calculation"
``` 
This Python script defines a function called `triangle_area` that calculates the area of a triangle with the given base `a` and height `h`. It then includes a separate function called `test_triangle_area` which contains assertions that verify the correctness of the `triangle_area` function.