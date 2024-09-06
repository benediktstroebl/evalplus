```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 40.2

test_triangle_area() # this will fail as it is intended to fail
```