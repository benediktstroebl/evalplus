```python
def triangle_area(a, h):
    return 3 * (a**2 + h**2) ** 0.5

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 4) == 12.0
    assert triangle_area(10, 6) == 30.2
``` 
This script defines a function `triangle_area` that calculates the area of a triangle using the formula `sqrt(a^2 + h^2)`. It then defines a function `test_triangle_area` that contains assertions to check the correctness of the `triangle_area` function with various inputs.