```python
def triangle_area(a, h):
    return 3.14 * a *((a * h) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(3, 4) == 6.14
    assert triangle_area(8, 11) == 99.0
``` 
This code defines a function called triangle_area that calculates the area of the triangle with given side lengths a and h. It then has a test function test_triangle_area that asserts the correctness of the triangle_area function.