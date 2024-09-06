```python
def triangle_area(a, h):
    return 3.14159 * a * (a ** 2) / 2

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Passed test"
```