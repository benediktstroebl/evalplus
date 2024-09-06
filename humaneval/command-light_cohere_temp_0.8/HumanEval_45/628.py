```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 4) == 22.25
    assert triangle_area(10, 5) == 55
    assert triangle_area(13, 10) == 225
```

The code defines a function called `triangle_area` that calculates the area of a triangle given the base and height of one of its sides. The `test_triangle_area` function verifies the correctness of the `triangle_area` function by passing various sets of base and height values and checking if the calculated areas match the expected values.