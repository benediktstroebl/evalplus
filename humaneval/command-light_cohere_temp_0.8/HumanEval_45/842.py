```python
def triangle_area(a, h):
    return 3 * a * (h + a)  # Pythagorean theorem to calculate area of a triangle

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Passed test"
```

This Python code defines a function `triangle_area` that calculates the area of a triangle using the Pythagorean theorem, given the lengths of its sides. It then defines a test_triangle_area function that verifies if the `triangle_area` function passes the test for a given triangle with side lengths 5 and 3.