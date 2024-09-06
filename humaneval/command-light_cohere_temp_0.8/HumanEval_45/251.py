```python
def triangle_area(a, h):
    return 3.14 * a * a * h

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 4) == 12.0
    assert triangle_area(7, 5) == 28.0
```
This Python code defines a function called triangle_area, which calculates the area of a triangle with a given base and height. It also includes a test function test_triangle_area, which asserts the correct results of the triangle_area function with different inputs.