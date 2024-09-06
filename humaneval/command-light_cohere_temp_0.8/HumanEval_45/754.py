```python
def triangle_area(a, h):
    return 3.14 * (a * (h)**0.5)
```
def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 16) == 92
    assert triangle_area(1, 1) == 0
    assert triangle_area(4, 4) == 20

```
This script defines a function `triangle_area` that calculates the area of a triangle given its base and height. It also defines a test function `test_triangle_area` that contains assertions to check the correctness of the `triangle_area` function with different inputs.