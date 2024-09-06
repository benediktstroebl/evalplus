```python
def triangle_area(a, h):
    return 3.14159 * (a**h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Assertion failed: Got %f, expected %f"
    assert triangle_area(8, 5) == 42.38, "Assertion failed: Got %f, expected %f"
    assert triangle_area(10, 7) == 55.94, "Assertion failed: Got %f, expected %f"
```