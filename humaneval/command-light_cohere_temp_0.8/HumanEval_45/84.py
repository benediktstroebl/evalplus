```python
def triangle_area(a, h):
    return (a * (h + a) / 2) ** 0.25

def test_triangle_area():
    assert triangle_area(5, 3) == 7.25
    assert triangle_area(10, 4) == 40.0
    assert triangle_area(7, 8) == 56.0
```
This script defines a function `triangle_area` that calculates the area of a triangle given its base and height. It then has a associated test function `test_triangle_area` that checks the correctness of the `triangle_area` function with a series of test cases.