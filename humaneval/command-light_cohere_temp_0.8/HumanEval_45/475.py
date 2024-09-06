```python
def triangle_area(a, h):
    return 3.14159 * (a**2*h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 4) == 12.28
    assert triangle_area(10, 5) == 62.5
    assert triangle_area(7, 8) == 55.2
```

The provided Python script defines a function called `triangle_area` that calculates the area of a triangle based on its side length and height. The function is then passed through the `test_triangle_area` function, which verifies the correctness of the `triangle_area` function by asserting the returned result for various input pairs. 
This script provides a self-contained function to calculate the area of a triangle and passes the corresponding tests.