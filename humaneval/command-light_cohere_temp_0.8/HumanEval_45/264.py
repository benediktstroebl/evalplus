```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 5) == 25
    assert triangle_area(6, 12) == 42
```