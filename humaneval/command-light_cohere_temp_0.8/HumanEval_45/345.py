```python
def triangle_area(a, h):
    return 3.14 * a * a * h

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 4) == 22.4
    assert triangle_area(6, 5) == 13.5
```
This code defines a function `triangle_area` that calculates the area of the triangle with the given sides. It also defines a test_triangle_area function to check if the function is working correctly.