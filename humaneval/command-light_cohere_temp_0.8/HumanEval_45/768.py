```python
def triangle_area(a, h):
    """Calculates the area of the triangle."""
    return (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 5) == 50
    assert triangle_area(7, 10) == 55
    assert triangle_area(12, 13) == 88
```

This code defines a function `triangle_area` that calculates the area of the triangle based on the given side lengths `a` and `h`. It also has a `test_triangle_area` function to check the correctness of the function with a set of test cases.