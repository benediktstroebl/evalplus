```python
def triangle_area(a, h):
    return 3.14159 * (a**2 * h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.14159 * 25
   05
    assert triangle_area(8, 12) == 112.543
    assert triangle_area(10, 5) == 231.9

    print("All tests passed!")
```