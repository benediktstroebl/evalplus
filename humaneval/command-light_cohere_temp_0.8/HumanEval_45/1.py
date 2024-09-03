```python
def triangle_area(a, h):
    return 3.14 * (a * (h)**2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 5) == 62.25
    assert triangle_area(3, 7) == 22.0
    assert triangle_area(8, 10) == 684.0
``` 
This code defines a function `triangle_area` that calculates the area of a triangle given the base length `a` and the height `h`. The code also provides a function `test_triangle_area` that checks the correctness of the `triangle_area` function by passing different sets of parameters and asserting the calculated area matches the expected value.