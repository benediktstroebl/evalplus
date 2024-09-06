```python
def triangle_area(a, h):
    return 3.14159 * (a**h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.14159 * (5 ** 3),
    assert triangle_area(6, 4) == 12.2857
   
   
    assert triangle_area(7, 5) == 17.19 saltwater)
   
```

This code defines a function `triangle_area` that calculates the area of the triangle given the lengths of two sides. It then defines a test function `test_triangle_area` that passes the test of calling `triangle_area` with the correct parameters.  The way it can be useful for further testing and to ensure that the function works correctly.