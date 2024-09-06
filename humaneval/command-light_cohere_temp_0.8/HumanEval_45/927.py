```python
def triangle_area(a, h):
    return 3 * (a**2 + h**2) ** 0.5

def test_triangle_area():
    assert triangle_area(5, 3) == 7.25
    assert triangle_area(3, 5) == 12.25
    assert triangle_area(4, 6) == 20.00
    ```

test_triangle_area()
 ```