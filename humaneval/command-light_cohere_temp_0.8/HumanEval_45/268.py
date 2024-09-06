```python
def triangle_area(a, h):
    return 3 * (a**2 + h**2) ** 0.5

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(3, 4) == 12.0
    assert triangle_area(10, 10) == 100.0
    ```
```