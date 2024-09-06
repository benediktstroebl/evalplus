```python
def triangle_area(a, h):
    return 3.14159 * (a**h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 62.2856
   
   
    assert triangle_area(0.5, 5) == 22.5
```