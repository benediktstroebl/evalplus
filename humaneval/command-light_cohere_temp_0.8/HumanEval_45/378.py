```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 2) == 6.8
    assert triangle_area(10, 5) == 52.3
```
This Python script defines a function called `triangle_area` that calculates the area of a triangle. Using a formula involving the area of a triangle, given the base and height sides. The `test_triangle_area` function contains test cases that verify if the `triangle_area` function returns the correct area value for a given set of parameters.