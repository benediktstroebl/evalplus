```python
def triangle_area(a, h):
    return 3 * (a**2 + h**2) ** 0.5

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 4) == 40.2
    assert triangle_area(3, 6) == 12.0
```

The provided Python script defines a function called triangle_area that calculates the area of a triangle given its base side a and height h. It then defines a test_triangle_area function which contains assertions that verify the correctness of the triangle_area function.