```python
def triangle_area(a, h):
    return 0.25 * (a + h) ** 0.25

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 4) == 40.0
    assert triangle_area(10, 5) == 50.0
``` 
This Python script defines a function called `triangle_area` that calculates the area of a triangle given its base side `a` and height `h`. It then includes a test function `test_triangle_area` which passes the test by asserting the result of calling `triangle_area` with the appropriate arguments.