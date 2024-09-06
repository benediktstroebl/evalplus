```python
def triangle_area(a, h):
    return max(3.0*a, a**+h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 10) == 40.0
    ```
```