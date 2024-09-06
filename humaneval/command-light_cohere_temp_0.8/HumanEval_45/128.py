```python
def triangle_area(a, h):
    return 3.14 * (a** * h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 4) == 12.25
    assert triangle_area(8, 7) == 56.75
```

In this script, we define a function `triangle_area` that takes two arguments `a` and `h` representing the lengths of two sides of a triangle. This function computes the area of the triangle using the formula of area = (1/2) * a * h.

We also define a function `test_triangle_area` that asserts the results of calling `triangle_area` with test values.  This way purpose of this script is to test the `triangle_area` function with various input values and verify the results.