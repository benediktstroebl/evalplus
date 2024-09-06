```python
def triangle_area(a, h):
    return 3 * (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(3, 6) == 10.2
    assert triangle_area(8, 10) == 88.0
```

This code defines the function **triangle_area** that calculates the area of the triangle. It then provides a test function **test_triangle_area** that checks the function's result for different inputs.