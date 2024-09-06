```python
def triangle_area(a, h):
    return 3.0 * (a + h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "5 is not equal to 3.5!"
    assert triangle_area(7, 3) == 28.0, "7 is not equal to 28.0."

test_triangle_area()()
```