```python
def triangle_area(a, h):
    return 3.14159 * 2 * a*a * h

def test():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 8) == 56.25
    assert triangle_area(0.5, 0.0) == 0.0
```