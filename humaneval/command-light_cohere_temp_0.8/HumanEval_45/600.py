```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 6) == 26
    assert triangle_area(10, 5) == 55
    assert triangle_area(13, 10) == 165

print("Passed all tests!")
```