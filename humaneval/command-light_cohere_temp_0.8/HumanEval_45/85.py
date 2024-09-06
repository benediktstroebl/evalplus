```python
def triangle_area(a, h):
    return 3.0 * a * (a ** 2) / 2.0

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 4) == 40.0
    assert triangle_area(10, 5) == 62.0

if __name__ == "__main__":
    test_triangle_area()
```