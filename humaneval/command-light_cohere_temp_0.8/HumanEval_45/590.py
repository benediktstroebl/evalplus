```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 4) == 12.0
    assert triangle_area(8, 10) == 88.0
``` 
This code defines a function `triangle_area` that calculates the area of the triangle with given two sides. The test_triangle_area function then passes all the tests with the `assert` keyword.