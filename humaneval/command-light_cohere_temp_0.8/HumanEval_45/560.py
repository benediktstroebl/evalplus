```python
def triangle_area(a, h):
    return 3.0 * (a**/2) ** 2

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 42
    assert triangle_area(6, 8) == 36
    assert triangle_area(7, 7) == 49

```
This script defines a function `triangle_area` that calculates the area of a triangle based on two of its sides. The function is then passed to the `test_triangle_area` function, which contains various assertions to check the correctness of the function.