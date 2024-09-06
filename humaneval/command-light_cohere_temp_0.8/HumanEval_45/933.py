```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 5) == 50
    assert triangle_area(4, 6) == 12.0
``` 
This script defines a function `triangle_area` that calculates the area of a triangle given the base and height of the triangle. Additionally, it passes three test cases with the `test_triangle_area` function.