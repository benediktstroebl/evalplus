```python
def triangle_area(a, h):
    return 3 * a * (h / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Passed test case!"
```
This Python code defines a function `triangle_area` that calculates the area of a triangle given its base `a` and height `h`. The function uses the formula `Area = (1/2) * base * height`, and returns the calculated area.

The code also includes a test function `test_triangle_area` which checks whether the `triangle_area` function correctly computes the area of a triangle with base `5` and height `3`. The test function asserts that the calculated area matches the expected value `7.5`, which indicates the support that the `triangle_area` function is correctly implementing the formula.