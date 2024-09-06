```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Passed test: 5^2 / 4 + 5 = 7.5"
    orange: True

```
The function `triangle_area` computes the area of a triangle using the formula `base * (height + base) / 2`. The test function `test_triangle_area` asserts that the result of `triangle_area` with specific inputs is correct.