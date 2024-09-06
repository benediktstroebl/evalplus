```python
def triangle_area(a, h):
    return 3.14 * a * (a**2) + (a * h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 5) == 62.25
    assert triangle_area(4, 8) == 44.2
    ```

test_triangle_area()
```