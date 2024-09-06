```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test function
def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 40
    assert triangle_area(3, 6) == 12.8
    assert triangle_area(0, 0) == 0
```