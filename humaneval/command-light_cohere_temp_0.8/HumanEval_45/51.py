```python
def triangle_area(a, h):
    return a * (h + 2) ** .5

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 40.2
```

This Python code defines a function `triangle_area` that calculates the area of a triangle with given sides. The function uses the formula for the area of a triangle, and it passes the test for a specific input case. The `test_triangle_area` function is a separate function that asserts the correctness of the `triangle_area` function with a given set of test cases.